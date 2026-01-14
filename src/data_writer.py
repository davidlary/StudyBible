"""
Data Writer Module

Handles atomic writing of verse JSON data to the file system.
Structure: data/{OT|NT}/{BOOK}/{CH}/{VS}.json

Functions:
    get_verse_path: Get file path for a verse
    write_verse_json: Write verse data to file
    atomic_write: Perform atomic file write
    verify_written_file: Verify file was written correctly
    get_testament_for_book: Determine testament (OT/NT) for a book
"""

import json
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional


# New Testament books for routing
NT_BOOKS = {
    "matthew", "mark", "luke", "john", "acts", "romans",
    "1corinthians", "1 corinthians", "2corinthians", "2 corinthians",
    "galatians", "ephesians", "philippians", "colossians",
    "1thessalonians", "1 thessalonians", "2thessalonians", "2 thessalonians",
    "1timothy", "1 timothy", "2timothy", "2 timothy", "titus", "philemon",
    "hebrews", "james", "1peter", "1 peter", "2peter", "2 peter",
    "1john", "1 john", "2john", "2 john", "3john", "3 john",
    "jude", "revelation"
}


def get_testament_for_book(book: str) -> str:
    """
    Determine testament (OT or NT) for a book.

    Args:
        book: Book name

    Returns:
        "OT" or "NT"
    """
    book_normalized = book.lower().strip()
    return "NT" if book_normalized in NT_BOOKS else "OT"


def get_verse_path(
    book: str,
    chapter: int,
    verse: int,
    base_path: Path
) -> Path:
    """
    Get file path for a verse JSON file.

    Path format: data/{OT|NT}/{BOOK}/{CH}/{VS}.json
    - Chapters are zero-padded to 2 digits
    - Verses are zero-padded to 2 digits

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        base_path: Base project directory

    Returns:
        Full path to verse JSON file
    """
    testament = get_testament_for_book(book)

    # Format chapter with zero-padding (2 digits)
    chapter_str = f"{chapter:02d}"

    # Format verse with zero-padding (2 digits)
    verse_str = f"{verse:02d}"

    # Build path
    path = base_path / "data" / testament / book / chapter_str / f"{verse_str}.json"

    return path


def atomic_write(target_path: Path, content: str) -> bool:
    """
    Perform atomic file write using temporary file.

    Writes to a temporary file first, then renames to target.
    This ensures partial writes don't corrupt data.

    Args:
        target_path: Target file path
        content: Content to write

    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure parent directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to temporary file in same directory
        tmp_path = target_path.with_suffix('.tmp')

        with open(tmp_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Atomic rename
        tmp_path.replace(target_path)

        return True

    except (IOError, OSError) as e:
        # Clean up temp file if it exists
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except:
                pass
        return False


def verify_written_file(
    file_path: Path,
    expected_data: Dict[str, Any]
) -> bool:
    """
    Verify that file was written correctly.

    Args:
        file_path: Path to written file
        expected_data: Expected data that should be in file

    Returns:
        True if file matches expected data, False otherwise
    """
    try:
        if not file_path.exists():
            return False

        with open(file_path, 'r', encoding='utf-8') as f:
            written_data = json.load(f)

        return written_data == expected_data

    except (IOError, OSError, json.JSONDecodeError):
        return False


def write_verse_json(
    book: str,
    chapter: int,
    verse: int,
    verse_data: Dict[str, Any],
    base_path: Path
) -> bool:
    """
    Write verse data to JSON file with atomic write.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        verse_data: Complete verse exegesis data
        base_path: Base project directory

    Returns:
        True if successful, False otherwise
    """
    try:
        # Get target path
        target_path = get_verse_path(book, chapter, verse, base_path)

        # Convert to pretty-printed JSON
        json_content = json.dumps(verse_data, indent=2, ensure_ascii=False)

        # Perform atomic write
        success = atomic_write(target_path, json_content)

        if not success:
            return False

        # Verify write
        return verify_written_file(target_path, verse_data)

    except Exception as e:
        return False

"""
Batch Processor Module

Processes multiple verses with checkpointing and progress tracking.

Functions:
    process_verse: Process a single verse (generate, validate, write)
    process_chapter: Process all verses in a chapter
    create_checkpoint: Save progress checkpoint
    load_checkpoint: Load saved checkpoint
    clear_checkpoint: Remove checkpoint file
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional

from src.exegesis_generator import generate_verse_exegesis
from src.schema_validator import validate_verse_json
from src.data_writer import write_verse_json
from src.bible_structure import get_verse_count


def process_verse(
    book: str,
    chapter: int,
    verse: int,
    config: Dict[str, Any]
) -> bool:
    """
    Process a single verse: generate, validate, and write.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        config: Configuration dict with paths and API key

    Returns:
        True if successful, False otherwise
    """
    # Generate exegesis
    exegesis_data = generate_verse_exegesis(
        book, chapter, verse,
        config["oshb_path"],
        config["sblgnt_path"],
        config["api_key"],
        config["study_prompt_path"]
    )

    if exegesis_data is None:
        return False

    # Validate against schema
    schema_path = config["base_path"] / "schemas" / "verse_schema.json"
    is_valid = validate_verse_json(exegesis_data, schema_path)

    if not is_valid:
        return False

    # Write to file
    success = write_verse_json(
        book, chapter, verse,
        exegesis_data,
        config["base_path"]
    )

    return success


def process_chapter(
    book: str,
    chapter: int,
    config: Dict[str, Any],
    start_verse: int = 1
) -> Dict[str, int]:
    """
    Process all verses in a chapter.

    Args:
        book: Book name
        chapter: Chapter number
        config: Configuration dict
        start_verse: Verse to start from (for resuming)

    Returns:
        Dict with processing results (total, successful, failed)
    """
    # Get verse count for chapter
    verse_count = get_verse_count(book, chapter)

    if verse_count is None:
        return {"total": 0, "successful": 0, "failed": 0}

    results = {
        "total": verse_count,
        "successful": 0,
        "failed": 0
    }

    # Process each verse
    for verse_num in range(start_verse, verse_count + 1):
        # Process verse
        success = process_verse(book, chapter, verse_num, config)

        if success:
            results["successful"] += 1
        else:
            results["failed"] += 1

        # Create checkpoint after each verse
        checkpoint_data = {
            "book": book,
            "chapter": chapter,
            "verse": verse_num,
            "completed": success
        }
        create_checkpoint(checkpoint_data, config["base_path"])

    return results


def create_checkpoint(checkpoint_data: Dict[str, Any], base_path: Path) -> None:
    """
    Save progress checkpoint to file.

    Args:
        checkpoint_data: Checkpoint data to save
        base_path: Base project directory
    """
    checkpoint_file = base_path / ".checkpoint.json"

    try:
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, indent=2)
    except (IOError, OSError):
        pass  # Silent fail for checkpoints


def load_checkpoint(base_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load saved checkpoint from file.

    Args:
        base_path: Base project directory

    Returns:
        Checkpoint data dict or None if no checkpoint
    """
    checkpoint_file = base_path / ".checkpoint.json"

    if not checkpoint_file.exists():
        return None

    try:
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, OSError, json.JSONDecodeError):
        return None


def clear_checkpoint(base_path: Path) -> None:
    """
    Remove checkpoint file.

    Args:
        base_path: Base project directory
    """
    checkpoint_file = base_path / ".checkpoint.json"

    try:
        if checkpoint_file.exists():
            checkpoint_file.unlink()
    except OSError:
        pass  # Silent fail

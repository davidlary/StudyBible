"""
Bible Structure - 66-Book Protestant Canon

Complete structure with chapter and verse counts for all 31,102 verses.
Data source: Standard Protestant Bible (39 OT + 27 NT books)
"""

from typing import Dict, Any, Optional, Iterator, Tuple
import logging

logger = logging.getLogger(__name__)

# Complete Bible structure with verse counts per chapter
BIBLE_STRUCTURE = {
    "OT": {
        "Genesis": {"abbr": "GEN", "chapters": 50, "verses": [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]},
        "Exodus": {"abbr": "EXO", "chapters": 40, "verses": [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]},
        "Leviticus": {"abbr": "LEV", "chapters": 27, "verses": [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]},
        "Numbers": {"abbr": "NUM", "chapters": 36, "verses": [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]},
        "Deuteronomy": {"abbr": "DEU", "chapters": 34, "verses": [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12]},
        "Joshua": {"abbr": "JOS", "chapters": 24, "verses": [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]},
        "Judges": {"abbr": "JDG", "chapters": 21, "verses": [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]},
        "Ruth": {"abbr": "RUT", "chapters": 4, "verses": [22, 23, 18, 22]},
        "1 Samuel": {"abbr": "1SA", "chapters": 31, "verses": [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13]},
        "2 Samuel": {"abbr": "2SA", "chapters": 24, "verses": [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]},
        "1 Kings": {"abbr": "1KI", "chapters": 22, "verses": [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53]},
        "2 Kings": {"abbr": "2KI", "chapters": 25, "verses": [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]},
        "1 Chronicles": {"abbr": "1CH", "chapters": 29, "verses": [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30]},
        "2 Chronicles": {"abbr": "2CH", "chapters": 36, "verses": [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]},
        "Ezra": {"abbr": "EZR", "chapters": 10, "verses": [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]},
        "Nehemiah": {"abbr": "NEH", "chapters": 13, "verses": [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]},
        "Esther": {"abbr": "EST", "chapters": 10, "verses": [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]},
        "Job": {"abbr": "JOB", "chapters": 42, "verses": [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17]},
        "Psalms": {"abbr": "PSA", "chapters": 150, "verses": [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6]},
        "Proverbs": {"abbr": "PRO", "chapters": 31, "verses": [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31]},
        "Ecclesiastes": {"abbr": "ECC", "chapters": 12, "verses": [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]},
        "Song of Solomon": {"abbr": "SNG", "chapters": 8, "verses": [17, 17, 11, 16, 16, 13, 13, 14]},
        "Isaiah": {"abbr": "ISA", "chapters": 66, "verses": [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]},
        "Jeremiah": {"abbr": "JER", "chapters": 52, "verses": [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]},
        "Lamentations": {"abbr": "LAM", "chapters": 5, "verses": [22, 22, 66, 22, 22]},
        "Ezekiel": {"abbr": "EZK", "chapters": 48, "verses": [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]},
        "Daniel": {"abbr": "DAN", "chapters": 12, "verses": [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]},
        "Hosea": {"abbr": "HOS", "chapters": 14, "verses": [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]},
        "Joel": {"abbr": "JOL", "chapters": 3, "verses": [20, 32, 21]},
        "Amos": {"abbr": "AMO", "chapters": 9, "verses": [15, 16, 15, 13, 27, 14, 17, 14, 15]},
        "Obadiah": {"abbr": "OBA", "chapters": 1, "verses": [21]},
        "Jonah": {"abbr": "JON", "chapters": 4, "verses": [17, 10, 10, 11]},
        "Micah": {"abbr": "MIC", "chapters": 7, "verses": [16, 13, 12, 13, 15, 16, 20]},
        "Nahum": {"abbr": "NAH", "chapters": 3, "verses": [15, 13, 19]},
        "Habakkuk": {"abbr": "HAB", "chapters": 3, "verses": [17, 20, 19]},
        "Zephaniah": {"abbr": "ZEP", "chapters": 3, "verses": [18, 15, 20]},
        "Haggai": {"abbr": "HAG", "chapters": 2, "verses": [15, 23]},
        "Zechariah": {"abbr": "ZEC", "chapters": 14, "verses": [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]},
        "Malachi": {"abbr": "MAL", "chapters": 4, "verses": [14, 17, 18, 6]}
    },
    "NT": {
        "Matthew": {"abbr": "MAT", "chapters": 28, "verses": [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20]},
        "Mark": {"abbr": "MAR", "chapters": 16, "verses": [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]},
        "Luke": {"abbr": "LUK", "chapters": 24, "verses": [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]},
        "John": {"abbr": "JOH", "chapters": 21, "verses": [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]},
        "Acts": {"abbr": "ACT", "chapters": 28, "verses": [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31]},
        "Romans": {"abbr": "ROM", "chapters": 16, "verses": [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]},
        "1 Corinthians": {"abbr": "1CO", "chapters": 16, "verses": [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]},
        "2 Corinthians": {"abbr": "2CO", "chapters": 13, "verses": [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]},
        "Galatians": {"abbr": "GAL", "chapters": 6, "verses": [24, 21, 29, 31, 26, 18]},
        "Ephesians": {"abbr": "EPH", "chapters": 6, "verses": [23, 22, 21, 32, 33, 24]},
        "Philippians": {"abbr": "PHP", "chapters": 4, "verses": [30, 30, 21, 23]},
        "Colossians": {"abbr": "COL", "chapters": 4, "verses": [29, 23, 25, 18]},
        "1 Thessalonians": {"abbr": "1TH", "chapters": 5, "verses": [10, 20, 13, 18, 28]},
        "2 Thessalonians": {"abbr": "2TH", "chapters": 3, "verses": [12, 17, 18]},
        "1 Timothy": {"abbr": "1TI", "chapters": 6, "verses": [20, 15, 16, 16, 25, 21]},
        "2 Timothy": {"abbr": "2TI", "chapters": 4, "verses": [18, 26, 17, 22]},
        "Titus": {"abbr": "TIT", "chapters": 3, "verses": [16, 15, 15]},
        "Philemon": {"abbr": "PHM", "chapters": 1, "verses": [25]},
        "Hebrews": {"abbr": "HEB", "chapters": 13, "verses": [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25]},
        "James": {"abbr": "JAS", "chapters": 5, "verses": [27, 26, 18, 17, 20]},
        "1 Peter": {"abbr": "1PE", "chapters": 5, "verses": [25, 25, 22, 19, 14]},
        "2 Peter": {"abbr": "2PE", "chapters": 3, "verses": [21, 22, 18]},
        "1 John": {"abbr": "1JO", "chapters": 5, "verses": [10, 29, 24, 21, 21]},
        "2 John": {"abbr": "2JO", "chapters": 1, "verses": [13]},
        "3 John": {"abbr": "3JO", "chapters": 1, "verses": [14]},
        "Jude": {"abbr": "JUD", "chapters": 1, "verses": [25]},
        "Revelation": {"abbr": "REV", "chapters": 22, "verses": [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21]}
    }
}


def get_book_info(book_name: str) -> Optional[Dict[str, Any]]:
    """
    Get complete information for a Bible book.

    Args:
        book_name: Name of the book (case-insensitive)

    Returns:
        Dict with book info including abbr, testament, chapters, verses
        None if book not found

    Example:
        >>> info = get_book_info("Genesis")
        >>> info["abbr"]
        'GEN'
        >>> info["chapters"]
        50
    """
    # Case-insensitive lookup
    book_name_lower = book_name.lower()

    for testament in ["OT", "NT"]:
        for name, data in BIBLE_STRUCTURE[testament].items():
            if name.lower() == book_name_lower:
                return {
                    "name": name,
                    "abbr": data["abbr"],
                    "testament": testament,
                    "chapters": data["chapters"],
                    "verses": data["verses"]
                }

    return None


def get_testament(book_name: str) -> Optional[str]:
    """
    Determine which testament a book belongs to.

    Args:
        book_name: Name of the book (case-insensitive)

    Returns:
        "OT" or "NT", or None if book not found
    """
    info = get_book_info(book_name)
    return info["testament"] if info else None


def get_verse_count(book_name: str, chapter: int) -> Optional[int]:
    """
    Get the number of verses in a specific chapter.

    Args:
        book_name: Name of the book
        chapter: Chapter number (1-indexed)

    Returns:
        Number of verses, or None if invalid

    Example:
        >>> get_verse_count("Genesis", 1)
        31
        >>> get_verse_count("Acts", 10)
        48
    """
    info = get_book_info(book_name)
    if not info:
        return None

    if chapter < 1 or chapter > info["chapters"]:
        return None

    # Verses list is 0-indexed, chapter is 1-indexed
    return info["verses"][chapter - 1]


def generate_verse_id(book_name: str, chapter: int, verse: int) -> str:
    """
    Generate standardized verse ID.

    Format: ABBR-CH-VS (e.g., "GEN-01-01", "ACT-10-48")

    Args:
        book_name: Name of the book
        chapter: Chapter number
        verse: Verse number

    Returns:
        Formatted verse ID string

    Example:
        >>> generate_verse_id("Genesis", 1, 1)
        'GEN-01-01'
        >>> generate_verse_id("Acts", 10, 48)
        'ACT-10-48'
    """
    info = get_book_info(book_name)
    if not info:
        raise ValueError(f"Invalid book name: {book_name}")

    abbr = info["abbr"]

    # Format with zero-padding
    # Most chapters are 2 digits, but Psalms has 150 chapters (3 digits)
    if info["chapters"] > 99:
        chapter_str = f"{chapter:03d}"
    else:
        chapter_str = f"{chapter:02d}"

    verse_str = f"{verse:02d}"

    return f"{abbr}-{chapter_str}-{verse_str}"


def validate_verse_reference(book_name: str, chapter: int, verse: int) -> bool:
    """
    Validate that a verse reference exists in the Bible.

    Args:
        book_name: Name of the book
        chapter: Chapter number
        verse: Verse number

    Returns:
        True if valid, False otherwise

    Example:
        >>> validate_verse_reference("Genesis", 1, 1)
        True
        >>> validate_verse_reference("Genesis", 51, 1)  # Only 50 chapters
        False
        >>> validate_verse_reference("Genesis", 1, 32)  # Only 31 verses
        False
    """
    info = get_book_info(book_name)
    if not info:
        return False

    if chapter < 1 or chapter > info["chapters"]:
        return False

    verse_count = get_verse_count(book_name, chapter)
    if verse_count is None:
        return False

    if verse < 1 or verse > verse_count:
        return False

    return True


def get_all_verses() -> Iterator[Tuple[str, int, int]]:
    """
    Generate all 31,102 verse references in canonical order.

    Yields:
        Tuple of (book_name, chapter, verse)

    Example:
        >>> verses = get_all_verses()
        >>> next(verses)
        ('Genesis', 1, 1)
        >>> len(list(get_all_verses()))
        31102
    """
    for testament in ["OT", "NT"]:
        for book_name, book_data in BIBLE_STRUCTURE[testament].items():
            chapters = book_data["chapters"]
            verses_per_chapter = book_data["verses"]

            for chapter_num in range(1, chapters + 1):
                verse_count = verses_per_chapter[chapter_num - 1]
                for verse_num in range(1, verse_count + 1):
                    yield (book_name, chapter_num, verse_num)


def get_total_verse_count() -> int:
    """
    Calculate total number of verses in the Bible.

    Returns:
        Total verse count (should be 31,102)

    Example:
        >>> get_total_verse_count()
        31102
    """
    total = 0
    for testament in ["OT", "NT"]:
        for book_data in BIBLE_STRUCTURE[testament].values():
            total += sum(book_data["verses"])

    return total


# Verify structure integrity on import
_total = get_total_verse_count()
if _total != 31102:
    logger.warning(f"Bible structure verification failed: Expected 31,102 verses, got {_total}")
else:
    logger.info(f"Bible structure loaded: 66 books, 31,102 verses")

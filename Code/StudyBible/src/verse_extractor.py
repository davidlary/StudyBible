"""
Verse Extractor Module

Extracts verse text from biblical source repositories:
- OSHB (Hebrew): XML parsing with lxml
- SBLGNT (Greek): Text file parsing

Functions:
    extract_hebrew_verse: Extract verse from OSHB XML
    extract_greek_verse: Extract verse from SBLGNT text
    extract_verse: Universal verse extractor (routes to correct source)
    book_name_to_osis_id: Convert book name to OSIS identifier
"""

from pathlib import Path
from typing import Optional
import re
from lxml import etree


# OSIS ID mappings for biblical books
BOOK_TO_OSIS = {
    # Old Testament
    "genesis": "Gen", "exodus": "Exod", "leviticus": "Lev", "numbers": "Num",
    "deuteronomy": "Deut", "joshua": "Josh", "judges": "Judg", "ruth": "Ruth",
    "1samuel": "1Sam", "2samuel": "2Sam", "1kings": "1Kgs", "2kings": "2Kgs",
    "1chronicles": "1Chr", "2chronicles": "2Chr", "ezra": "Ezra", "nehemiah": "Neh",
    "esther": "Esth", "job": "Job", "psalms": "Ps", "proverbs": "Prov",
    "ecclesiastes": "Eccl", "songofsolomon": "Song", "isaiah": "Isa",
    "jeremiah": "Jer", "lamentations": "Lam", "ezekiel": "Ezek", "daniel": "Dan",
    "hosea": "Hos", "joel": "Joel", "amos": "Amos", "obadiah": "Obad",
    "jonah": "Jonah", "micah": "Mic", "nahum": "Nah", "habakkuk": "Hab",
    "zephaniah": "Zeph", "haggai": "Hag", "zechariah": "Zech", "malachi": "Mal",
    # New Testament
    "matthew": "Matt", "mark": "Mark", "luke": "Luke", "john": "John",
    "acts": "Acts", "romans": "Rom", "1corinthians": "1Cor", "2corinthians": "2Cor",
    "galatians": "Gal", "ephesians": "Eph", "philippians": "Phil", "colossians": "Col",
    "1thessalonians": "1Thess", "2thessalonians": "2Thess", "1timothy": "1Tim",
    "2timothy": "2Tim", "titus": "Titus", "philemon": "Phlm", "hebrews": "Heb",
    "james": "Jas", "1peter": "1Pet", "2peter": "2Pet", "1john": "1John",
    "2john": "2John", "3john": "3John", "jude": "Jude", "revelation": "Rev",
}

# SBLGNT book number to name mapping
SBLGNT_BOOK_NUMBERS = {
    40: "Matthew", 41: "Mark", 42: "Luke", 43: "John", 44: "Acts",
    45: "Romans", 46: "1Corinthians", 47: "2Corinthians", 48: "Galatians",
    49: "Ephesians", 50: "Philippians", 51: "Colossians", 52: "1Thessalonians",
    53: "2Thessalonians", 54: "1Timothy", 55: "2Timothy", 56: "Titus",
    57: "Philemon", 58: "Hebrews", 59: "James", 60: "1Peter", 61: "2Peter",
    62: "1John", 63: "2John", 64: "3John", 65: "Jude", 66: "Revelation",
}

# Reverse mapping for SBLGNT
BOOK_TO_SBLGNT_NUMBER = {v.lower(): k for k, v in SBLGNT_BOOK_NUMBERS.items()}

# New Testament books (for routing)
NT_BOOKS = {
    "matthew", "mark", "luke", "john", "acts", "romans", "1corinthians",
    "2corinthians", "galatians", "ephesians", "philippians", "colossians",
    "1thessalonians", "2thessalonians", "1timothy", "2timothy", "titus",
    "philemon", "hebrews", "james", "1peter", "2peter", "1john", "2john",
    "3john", "jude", "revelation",
}


def book_name_to_osis_id(book_name: str) -> Optional[str]:
    """
    Convert book name to OSIS identifier.

    Args:
        book_name: Name of biblical book (case insensitive)

    Returns:
        OSIS ID string or None if invalid
    """
    normalized = book_name.lower().replace(" ", "")
    return BOOK_TO_OSIS.get(normalized)


def extract_hebrew_verse(
    book: str,
    chapter: int,
    verse: int,
    oshb_path: Path,
    strip_marks: bool = False
) -> Optional[str]:
    """
    Extract Hebrew verse text from OSHB XML.

    Args:
        book: Book name (e.g., "Genesis")
        chapter: Chapter number
        verse: Verse number
        oshb_path: Path to OSHB directory or XML file
        strip_marks: If True, remove cantillation marks

    Returns:
        Hebrew text string or None if not found
    """
    try:
        # Convert book name to OSIS ID
        osis_id = book_name_to_osis_id(book)
        if not osis_id:
            return None

        # If path is directory, look for the book file
        if oshb_path.is_dir():
            # OSHB structure: wlc/Genesis.xml or similar
            xml_file = oshb_path / "wlc" / f"{osis_id}.xml"
            if not xml_file.exists():
                # Try alternate location
                xml_file = oshb_path / f"{osis_id}.xml"
        else:
            xml_file = oshb_path

        if not xml_file.exists():
            return None

        # Parse XML
        tree = etree.parse(str(xml_file))
        root = tree.getroot()

        # Define namespace
        ns = {"osis": "http://www.bibletechnologies.net/2003/OSIS/namespace"}

        # Build verse ID (e.g., "Gen.1.1")
        verse_id = f"{osis_id}.{chapter}.{verse}"

        # Find the verse element
        verse_elem = root.find(f".//osis:verse[@osisID='{verse_id}']", ns)

        if verse_elem is None:
            return None

        # Extract all word elements
        words = verse_elem.findall(".//osis:w", ns)

        # Get text from each word
        text_parts = []
        for word in words:
            if word.text:
                text_parts.append(word.text)

        if not text_parts:
            return None

        # Join with spaces
        hebrew_text = " ".join(text_parts)

        # Optionally strip cantillation marks
        if strip_marks:
            # Remove cantillation marks (Unicode range U+0591 to U+05BD, U+05BF to U+05C7)
            hebrew_text = re.sub(r'[\u0591-\u05bd\u05bf-\u05c7]', '', hebrew_text)

        return hebrew_text

    except (etree.XMLSyntaxError, IOError, OSError) as e:
        return None


def extract_greek_verse(
    book: str,
    chapter: int,
    verse: int,
    sblgnt_path: Path
) -> Optional[str]:
    """
    Extract Greek verse text from SBLGNT text file.

    SBLGNT format: Each line has fields separated by spaces:
    [book_num] [pos] [parsing] [text] [word] [normalized] [lemma] ...

    Args:
        book: Book name (e.g., "Acts")
        chapter: Chapter number
        verse: Verse number
        sblgnt_path: Path to SBLGNT directory or text file

    Returns:
        Greek text string or None if not found
    """
    try:
        # Get SBLGNT book number
        book_normalized = book.lower().replace(" ", "")
        book_num = BOOK_TO_SBLGNT_NUMBER.get(book_normalized)

        if book_num is None:
            return None

        # If path is directory, look for the book file
        if sblgnt_path.is_dir():
            # Try multiple possible locations for SBLGNT text files
            # Format 1: data/sblgnt/text/BookName.txt (Faithlife/SBLGNT)
            text_file = sblgnt_path / "data" / "sblgnt" / "text" / f"{book}.txt"
            if not text_file.exists():
                # Format 2: sblgnt.txt (MorphGNT combined file)
                text_file = sblgnt_path / "sblgnt.txt"
            if not text_file.exists():
                # Format 3: data/sblgnt.txt
                text_file = sblgnt_path / "data" / "sblgnt.txt"
        else:
            text_file = sblgnt_path

        if not text_file.exists():
            return None

        # Read and parse the file
        # Try tab-delimited format first (Faithlife/SBLGNT): "Acts 1:1<tab>Greek text"
        verse_ref = f"{book} {chapter}:{verse}"
        with open(text_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Try tab-delimited format
                if '\t' in line:
                    parts = line.split('\t', 1)
                    if len(parts) == 2 and parts[0] == verse_ref:
                        return parts[1].strip()
                else:
                    # Try space-delimited MorphGNT format: book_num chapter verse word ...
                    parts = line.split()
                    if len(parts) < 4:
                        continue

                    try:
                        line_book = int(parts[0])
                        line_chapter = int(parts[1])
                        line_verse = int(parts[2])
                        word_text = parts[3]

                        # Check if this is our verse
                        if (line_book == book_num and
                            line_chapter == chapter and
                            line_verse == verse):
                            return word_text

                    except (ValueError, IndexError):
                        continue

        return None

    except (IOError, OSError) as e:
        return None


def extract_verse(
    book: str,
    chapter: int,
    verse: int,
    oshb_path: Path,
    sblgnt_path: Path
) -> Optional[str]:
    """
    Universal verse extractor that routes to correct source.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        oshb_path: Path to OSHB directory
        sblgnt_path: Path to SBLGNT directory

    Returns:
        Verse text (Hebrew or Greek) or None if not found
    """
    book_normalized = book.lower().replace(" ", "")

    # Route to correct extractor
    if book_normalized in NT_BOOKS:
        return extract_greek_verse(book, chapter, verse, sblgnt_path)
    else:
        return extract_hebrew_verse(book, chapter, verse, oshb_path)

"""
Exegesis Generator Module

Orchestrates the generation of biblical exegesis by:
1. Loading study prompt template
2. Extracting verse text from sources
3. Building complete prompt
4. Calling Gemini API
5. Returning structured exegesis data

Functions:
    load_study_prompt: Load StudyPrompt.md template
    build_exegesis_prompt: Build complete prompt for a verse
    generate_verse_exegesis: Generate exegesis for a single verse
    format_verse_reference: Format verse reference (Genesis 1:1)
    format_verse_id: Format verse ID (GEN-1-1)
"""

from pathlib import Path
from typing import Optional, Dict, Any

# Import required modules
from src.verse_extractor import extract_verse
from src.gemini_client import generate_exegesis


def load_study_prompt(prompt_path: Path) -> str:
    """
    Load the StudyPrompt.md template.

    Args:
        prompt_path: Path to StudyPrompt.md file

    Returns:
        Prompt template text

    Raises:
        FileNotFoundError: If prompt file doesn't exist
        IOError: If file cannot be read
    """
    if not prompt_path.exists():
        raise FileNotFoundError(f"Study prompt not found: {prompt_path}")

    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()


def format_verse_reference(book: str, chapter: int, verse: int) -> str:
    """
    Format verse reference for display (e.g., "Genesis 1:1").

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number

    Returns:
        Formatted reference string
    """
    return f"{book} {chapter}:{verse}"


def format_verse_id(book: str, chapter: int, verse: int) -> str:
    """
    Format verse ID for storage (e.g., "GEN-1-1").

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number

    Returns:
        Formatted verse ID string
    """
    # Remove spaces and convert to uppercase
    book_normalized = book.replace(" ", "").upper()

    # Abbreviate common books
    abbreviations = {
        "GENESIS": "GEN",
        "EXODUS": "EXO",
        "LEVITICUS": "LEV",
        "NUMBERS": "NUM",
        "DEUTERONOMY": "DEU",
        "1CORINTHIANS": "1COR",
        "2CORINTHIANS": "2COR",
        "1THESSALONIANS": "1TH",
        "2THESSALONIANS": "2TH",
        "1TIMOTHY": "1TIM",
        "2TIMOTHY": "2TIM",
        "1PETER": "1PET",
        "2PETER": "2PET",
        "1JOHN": "1JN",
        "2JOHN": "2JN",
        "3JOHN": "3JN",
        "SONGOFSOLOMON": "SONG",
    }

    book_id = abbreviations.get(book_normalized, book_normalized)

    return f"{book_id}-{chapter}-{verse}"


def build_exegesis_prompt(
    book: str,
    chapter: int,
    verse: int,
    verse_text: str,
    study_prompt_path: Path
) -> str:
    """
    Build complete exegesis prompt for Gemini API.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        verse_text: Original language verse text
        study_prompt_path: Path to StudyPrompt.md

    Returns:
        Complete prompt string
    """
    # Load study prompt template
    study_instructions = load_study_prompt(study_prompt_path)

    # Format verse reference
    verse_ref = format_verse_reference(book, chapter, verse)
    verse_id = format_verse_id(book, chapter, verse)

    # Build complete prompt
    prompt = f"""
{study_instructions}

---

## VERSE TO ANALYZE

**Reference:** {verse_ref}
**Verse ID:** {verse_id}
**Original Text:** {verse_text}

---

## INSTRUCTIONS

Generate a complete, high-fidelity exegetical analysis for {verse_ref} following ALL requirements in the study prompt above.

Output the result as a single, valid JSON object matching the verse schema structure.

Ensure you include:
1. All four translations in section_1_sacred_text
2. All ten required subsections in section_2_exegetical_synthesis
3. A practical life application in section_3_life_application

The verse_id field MUST be: {verse_id}

Begin your JSON output now:
"""

    return prompt


def generate_verse_exegesis(
    book: str,
    chapter: int,
    verse: int,
    oshb_path: Path,
    sblgnt_path: Path,
    api_key: str,
    study_prompt_path: Path,
    max_retries: int = 3
) -> Optional[Dict[str, Any]]:
    """
    Generate complete exegesis for a single verse.

    Args:
        book: Book name
        chapter: Chapter number
        verse: Verse number
        oshb_path: Path to OSHB directory
        sblgnt_path: Path to SBLGNT directory
        api_key: Gemini API key
        study_prompt_path: Path to StudyPrompt.md
        max_retries: Maximum API retry attempts

    Returns:
        Complete exegesis data dict or None if failed
    """
    # Extract verse text from sources
    verse_text = extract_verse(book, chapter, verse, oshb_path, sblgnt_path)

    if verse_text is None:
        return None

    # Build complete prompt
    prompt = build_exegesis_prompt(book, chapter, verse, verse_text, study_prompt_path)

    # Call Gemini API
    exegesis_data = generate_exegesis(prompt, api_key, max_retries=max_retries)

    return exegesis_data

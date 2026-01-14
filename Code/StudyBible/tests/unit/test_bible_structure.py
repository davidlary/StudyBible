"""
Unit tests for src/bible_structure.py

Defines expected behavior for 66-book Protestant canon structure.
"""

import pytest
from typing import Iterator, Tuple


@pytest.mark.unit
class TestBibleStructure:
    """Test Bible structure and metadata"""

    def test_bible_has_66_books(self):
        """Test that Protestant canon has exactly 66 books"""
        from src.bible_structure import BIBLE_STRUCTURE

        total_books = len(BIBLE_STRUCTURE["OT"]) + len(BIBLE_STRUCTURE["NT"])
        assert total_books == 66, f"Expected 66 books, got {total_books}"

    def test_old_testament_has_39_books(self):
        """Test that Old Testament has 39 books"""
        from src.bible_structure import BIBLE_STRUCTURE

        ot_books = len(BIBLE_STRUCTURE["OT"])
        assert ot_books == 39, f"Expected 39 OT books, got {ot_books}"

    def test_new_testament_has_27_books(self):
        """Test that New Testament has 27 books"""
        from src.bible_structure import BIBLE_STRUCTURE

        nt_books = len(BIBLE_STRUCTURE["NT"])
        assert nt_books == 27, f"Expected 27 NT books, got {nt_books}"

    def test_total_verses_is_31102(self):
        """Test that total verses equals 31,102"""
        from src.bible_structure import get_total_verse_count

        total = get_total_verse_count()
        assert total == 31102, f"Expected 31,102 verses, got {total}"

    def test_get_book_info_genesis(self):
        """Test retrieving info for Genesis"""
        from src.bible_structure import get_book_info

        info = get_book_info("Genesis")
        assert info is not None
        assert info["abbr"] == "GEN"
        assert info["testament"] == "OT"
        assert info["chapters"] == 50
        assert len(info["verses"]) == 50  # 50 chapters

    def test_get_book_info_acts(self):
        """Test retrieving info for Acts"""
        from src.bible_structure import get_book_info

        info = get_book_info("Acts")
        assert info is not None
        assert info["abbr"] == "ACT"
        assert info["testament"] == "NT"
        assert info["chapters"] == 28
        assert len(info["verses"]) == 28  # 28 chapters

    def test_get_book_info_case_insensitive(self):
        """Test that book lookup is case-insensitive"""
        from src.bible_structure import get_book_info

        info1 = get_book_info("genesis")
        info2 = get_book_info("GENESIS")
        info3 = get_book_info("Genesis")

        assert info1 == info2 == info3
        assert info1["abbr"] == "GEN"

    def test_get_book_info_invalid_returns_none(self):
        """Test that invalid book name returns None"""
        from src.bible_structure import get_book_info

        info = get_book_info("NotABook")
        assert info is None

    def test_get_verse_count_genesis_1(self):
        """Test verse count for Genesis 1"""
        from src.bible_structure import get_verse_count

        count = get_verse_count("Genesis", 1)
        assert count == 31  # Genesis 1 has 31 verses

    def test_get_verse_count_acts_10(self):
        """Test verse count for Acts 10"""
        from src.bible_structure import get_verse_count

        count = get_verse_count("Acts", 10)
        assert count == 48  # Acts 10 has 48 verses

    def test_get_verse_count_psalm_119(self):
        """Test verse count for Psalm 119 (longest chapter)"""
        from src.bible_structure import get_verse_count

        count = get_verse_count("Psalms", 119)
        assert count == 176  # Psalm 119 has 176 verses (longest)

    def test_generate_verse_id_genesis(self):
        """Test generating verse ID for Genesis 1:1"""
        from src.bible_structure import generate_verse_id

        verse_id = generate_verse_id("Genesis", 1, 1)
        assert verse_id == "GEN-01-01"

    def test_generate_verse_id_acts(self):
        """Test generating verse ID for Acts 10:48"""
        from src.bible_structure import generate_verse_id

        verse_id = generate_verse_id("Acts", 10, 48)
        assert verse_id == "ACT-10-48"

    def test_generate_verse_id_formats_correctly(self):
        """Test that verse IDs are formatted with zero-padding"""
        from src.bible_structure import generate_verse_id

        # Single-digit chapter and verse
        assert generate_verse_id("Matthew", 5, 3) == "MAT-05-03"

        # Double-digit chapter and verse
        assert generate_verse_id("John", 21, 25) == "JOH-21-25"

        # Triple-digit chapter (Psalms)
        assert generate_verse_id("Psalms", 150, 6) == "PSA-150-06"

    def test_validate_verse_reference_valid(self):
        """Test validating valid verse references"""
        from src.bible_structure import validate_verse_reference

        assert validate_verse_reference("Genesis", 1, 1) is True
        assert validate_verse_reference("Acts", 10, 48) is True
        assert validate_verse_reference("Psalms", 119, 176) is True

    def test_validate_verse_reference_invalid_book(self):
        """Test validating invalid book name"""
        from src.bible_structure import validate_verse_reference

        assert validate_verse_reference("NotABook", 1, 1) is False

    def test_validate_verse_reference_invalid_chapter(self):
        """Test validating invalid chapter number"""
        from src.bible_structure import validate_verse_reference

        assert validate_verse_reference("Genesis", 51, 1) is False  # Genesis has 50 chapters
        assert validate_verse_reference("Genesis", 0, 1) is False  # Chapter 0 doesn't exist

    def test_validate_verse_reference_invalid_verse(self):
        """Test validating invalid verse number"""
        from src.bible_structure import validate_verse_reference

        assert validate_verse_reference("Genesis", 1, 32) is False  # Genesis 1 has 31 verses
        assert validate_verse_reference("Genesis", 1, 0) is False  # Verse 0 doesn't exist

    def test_get_all_verses_returns_iterator(self):
        """Test that get_all_verses returns an iterator"""
        from src.bible_structure import get_all_verses

        verses = get_all_verses()
        assert isinstance(verses, Iterator)

    def test_get_all_verses_count(self):
        """Test that get_all_verses yields 31,102 verses"""
        from src.bible_structure import get_all_verses

        verses = list(get_all_verses())
        assert len(verses) == 31102

    def test_get_all_verses_format(self):
        """Test that each verse is (book, chapter, verse) tuple"""
        from src.bible_structure import get_all_verses

        verses = get_all_verses()
        first_verse = next(verses)

        assert isinstance(first_verse, tuple)
        assert len(first_verse) == 3
        book, chapter, verse = first_verse
        assert isinstance(book, str)
        assert isinstance(chapter, int)
        assert isinstance(verse, int)

    def test_get_all_verses_starts_with_genesis(self):
        """Test that iteration starts with Genesis 1:1"""
        from src.bible_structure import get_all_verses

        verses = get_all_verses()
        first_verse = next(verses)
        book, chapter, verse = first_verse

        assert book == "Genesis"
        assert chapter == 1
        assert verse == 1

    def test_get_testament_for_book(self):
        """Test determining testament for a book"""
        from src.bible_structure import get_testament

        assert get_testament("Genesis") == "OT"
        assert get_testament("Matthew") == "NT"
        assert get_testament("Acts") == "NT"
        assert get_testament("Malachi") == "OT"

    def test_get_testament_case_insensitive(self):
        """Test that testament lookup is case-insensitive"""
        from src.bible_structure import get_testament

        assert get_testament("genesis") == "OT"
        assert get_testament("ACTS") == "NT"

    def test_get_testament_invalid_returns_none(self):
        """Test that invalid book returns None"""
        from src.bible_structure import get_testament

        assert get_testament("NotABook") is None

    def test_book_abbreviations_unique(self):
        """Test that all book abbreviations are unique"""
        from src.bible_structure import BIBLE_STRUCTURE

        abbreviations = set()
        for testament in ["OT", "NT"]:
            for book_name, book_data in BIBLE_STRUCTURE[testament].items():
                abbr = book_data["abbr"]
                assert abbr not in abbreviations, f"Duplicate abbreviation: {abbr}"
                abbreviations.add(abbr)

        assert len(abbreviations) == 66

    def test_specific_book_verse_counts(self):
        """Test verse counts for specific well-known chapters"""
        from src.bible_structure import get_verse_count

        # John 3:16 is famous - John 3 should have at least 16 verses
        assert get_verse_count("John", 3) >= 16

        # Psalm 23 is famous - Psalm 23 should have 6 verses
        assert get_verse_count("Psalms", 23) == 6

        # Romans 8 is important - Romans 8 should have 39 verses
        assert get_verse_count("Romans", 8) == 39

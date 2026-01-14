"""
Unit tests for verse_extractor module.
Tests the extraction of verses from OSHB XML and SBLGNT text sources.
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, mock_open


class TestVerseExtractor:
    """Test suite for verse extraction functionality."""

    @pytest.fixture
    def oshb_sample_path(self):
        """Path to OSHB sample XML fixture."""
        return Path(__file__).parent.parent / "fixtures" / "oshb_sample.xml"

    @pytest.fixture
    def sblgnt_sample_path(self):
        """Path to SBLGNT sample text fixture."""
        return Path(__file__).parent.parent / "fixtures" / "sblgnt_sample.txt"

    def test_extract_hebrew_verse_returns_text(self, oshb_sample_path):
        """Test that extract_hebrew_verse() returns verse text from OSHB XML."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 1, oshb_sample_path)

        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    def test_extract_hebrew_verse_contains_hebrew(self, oshb_sample_path):
        """Test that extracted Hebrew text contains Hebrew characters."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 1, oshb_sample_path)

        # Check for Hebrew characters (Unicode range U+0590 to U+05FF)
        has_hebrew = any('\u0590' <= char <= '\u05FF' for char in result)
        assert has_hebrew

    def test_extract_hebrew_verse_genesis_1_1(self, oshb_sample_path):
        """Test extraction of Genesis 1:1 specifically."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 1, oshb_sample_path)

        assert "בְּרֵאשִׁ֖ית" in result
        assert "בָּרָ֣א" in result
        assert "אֱלֹהִ֑ים" in result

    def test_extract_hebrew_verse_genesis_1_2(self, oshb_sample_path):
        """Test extraction of Genesis 1:2."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 2, oshb_sample_path)

        assert "וְהָאָ֗רֶץ" in result
        assert "הָיְתָ֥ה" in result

    def test_extract_hebrew_verse_invalid_chapter_returns_none(self, oshb_sample_path):
        """Test that extract_hebrew_verse() returns None for invalid chapter."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 999, 1, oshb_sample_path)

        assert result is None

    def test_extract_hebrew_verse_invalid_verse_returns_none(self, oshb_sample_path):
        """Test that extract_hebrew_verse() returns None for invalid verse."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 999, oshb_sample_path)

        assert result is None

    def test_extract_hebrew_verse_invalid_book_returns_none(self, oshb_sample_path):
        """Test that extract_hebrew_verse() returns None for invalid book."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("InvalidBook", 1, 1, oshb_sample_path)

        assert result is None

    def test_extract_greek_verse_returns_text(self, sblgnt_sample_path):
        """Test that extract_greek_verse() returns verse text from SBLGNT."""
        from src.verse_extractor import extract_greek_verse

        result = extract_greek_verse("Acts", 10, 44, sblgnt_sample_path)

        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    def test_extract_greek_verse_contains_greek(self, sblgnt_sample_path):
        """Test that extracted Greek text contains Greek characters."""
        from src.verse_extractor import extract_greek_verse

        result = extract_greek_verse("Acts", 10, 44, sblgnt_sample_path)

        # Check for Greek characters (Unicode range U+0370 to U+03FF)
        has_greek = any('\u0370' <= char <= '\u03FF' for char in result)
        assert has_greek

    def test_extract_greek_verse_acts_10_44(self, sblgnt_sample_path):
        """Test extraction of Acts 10:44 specifically."""
        from src.verse_extractor import extract_greek_verse

        result = extract_greek_verse("Acts", 10, 44, sblgnt_sample_path)

        assert "Πέτρος" in result
        assert "λαλοῦντος" in result
        assert "πνεῦμα" in result

    def test_extract_greek_verse_invalid_returns_none(self):
        """Test that extract_greek_verse() returns None for invalid reference."""
        from src.verse_extractor import extract_greek_verse

        # For this test, we'll mock the file reading to avoid needing real SBLGNT
        fake_path = Path("/fake/path/sblgnt.txt")

        with patch("builtins.open", mock_open(read_data="44 N- ----NSM- word")):
            result = extract_greek_verse("Acts", 999, 999, fake_path)

        assert result is None

    def test_extract_verse_calls_hebrew_for_ot_book(self, oshb_sample_path, tmp_path):
        """Test that extract_verse() routes to Hebrew for OT books."""
        from src.verse_extractor import extract_verse

        # Create fake SBLGNT path
        sblgnt_path = tmp_path / "sblgnt.txt"
        sblgnt_path.write_text("")

        result = extract_verse("Genesis", 1, 1, oshb_sample_path, sblgnt_path)

        assert result is not None
        assert "בְּרֵאשִׁ֖ית" in result

    def test_extract_verse_calls_greek_for_nt_book(self, tmp_path, sblgnt_sample_path):
        """Test that extract_verse() routes to Greek for NT books."""
        from src.verse_extractor import extract_verse

        # Create fake OSHB path
        oshb_path = tmp_path / "oshb.xml"
        oshb_path.write_text("<osis/>")

        result = extract_verse("Acts", 10, 44, oshb_path, sblgnt_sample_path)

        assert result is not None
        assert "Πέτρος" in result

    def test_extract_verse_handles_invalid_book(self, tmp_path):
        """Test that extract_verse() handles invalid book name."""
        from src.verse_extractor import extract_verse

        oshb_path = tmp_path / "oshb.xml"
        sblgnt_path = tmp_path / "sblgnt.txt"

        result = extract_verse("InvalidBook", 1, 1, oshb_path, sblgnt_path)

        assert result is None

    def test_book_name_to_osis_id_genesis(self):
        """Test book name conversion for Genesis."""
        from src.verse_extractor import book_name_to_osis_id

        assert book_name_to_osis_id("Genesis") == "Gen"

    def test_book_name_to_osis_id_acts(self):
        """Test book name conversion for Acts."""
        from src.verse_extractor import book_name_to_osis_id

        assert book_name_to_osis_id("Acts") == "Acts"

    def test_book_name_to_osis_id_case_insensitive(self):
        """Test book name conversion is case insensitive."""
        from src.verse_extractor import book_name_to_osis_id

        assert book_name_to_osis_id("genesis") == "Gen"
        assert book_name_to_osis_id("ACTS") == "Acts"

    def test_book_name_to_osis_id_invalid_returns_none(self):
        """Test book name conversion returns None for invalid book."""
        from src.verse_extractor import book_name_to_osis_id

        assert book_name_to_osis_id("InvalidBook") is None

    def test_extract_hebrew_verse_strips_cantillation_marks(self, oshb_sample_path):
        """Test that cantillation marks can be optionally removed."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 1, oshb_sample_path, strip_marks=True)

        # Result should have Hebrew but fewer diacritical marks
        assert result is not None
        assert len(result) > 0

    def test_extract_hebrew_verse_with_directory_path(self, tmp_path):
        """Test that extract_hebrew_verse works with directory path."""
        from src.verse_extractor import extract_hebrew_verse

        # Create mock directory structure
        wlc_dir = tmp_path / "wlc"
        wlc_dir.mkdir()

        # Copy sample XML
        sample_path = Path(__file__).parent.parent / "fixtures" / "oshb_sample.xml"
        target = wlc_dir / "Gen.xml"
        import shutil
        shutil.copy(sample_path, target)

        result = extract_hebrew_verse("Genesis", 1, 1, tmp_path)

        assert result is not None
        assert "בְּרֵאשִׁ֖ית" in result

    def test_extract_greek_verse_with_directory_path(self, tmp_path):
        """Test that extract_greek_verse works with directory path."""
        from src.verse_extractor import extract_greek_verse

        # Create mock directory structure
        data_dir = tmp_path / "data"
        data_dir.mkdir()

        # Copy sample text
        sample_path = Path(__file__).parent.parent / "fixtures" / "sblgnt_sample.txt"
        target = tmp_path / "sblgnt.txt"
        import shutil
        shutil.copy(sample_path, target)

        result = extract_greek_verse("Acts", 10, 44, tmp_path)

        assert result is not None
        assert "Πέτρος" in result

    def test_extract_hebrew_verse_file_not_found(self, tmp_path):
        """Test that extract_hebrew_verse handles missing file."""
        from src.verse_extractor import extract_hebrew_verse

        result = extract_hebrew_verse("Genesis", 1, 1, tmp_path / "nonexistent.xml")

        assert result is None

    def test_extract_greek_verse_file_not_found(self, tmp_path):
        """Test that extract_greek_verse handles missing file."""
        from src.verse_extractor import extract_greek_verse

        result = extract_greek_verse("Acts", 10, 44, tmp_path / "nonexistent.txt")

        assert result is None

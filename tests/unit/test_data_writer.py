"""
Unit tests for data_writer module.
Tests atomic writing of verse JSON data to file system.
"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch, mock_open


class TestDataWriter:
    """Test suite for data writing functionality."""

    @pytest.fixture
    def sample_verse_data(self):
        """Sample verse data for testing."""
        return {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "original_script": "בְּרֵאשִׁית",
                "faithful_direct_translation": "In beginning",
                "standalone_english_translation": "In the beginning",
                "amplified_narrative_translation": "At the beginning"
            },
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": "Application"
        }

    def test_get_verse_path_ot_book(self, tmp_path):
        """Test that get_verse_path() returns correct path for OT book."""
        from src.data_writer import get_verse_path

        path = get_verse_path("Genesis", 1, 1, tmp_path)

        assert str(path).endswith("data/OT/Genesis/01/01.json")
        assert isinstance(path, Path)

    def test_get_verse_path_nt_book(self, tmp_path):
        """Test that get_verse_path() returns correct path for NT book."""
        from src.data_writer import get_verse_path

        path = get_verse_path("Acts", 10, 44, tmp_path)

        assert str(path).endswith("data/NT/Acts/10/44.json")
        assert isinstance(path, Path)

    def test_get_verse_path_formats_single_digit_chapter(self, tmp_path):
        """Test that get_verse_path() zero-pads single-digit chapters."""
        from src.data_writer import get_verse_path

        path = get_verse_path("Genesis", 1, 1, tmp_path)

        assert "/01/" in str(path)

    def test_get_verse_path_formats_double_digit_chapter(self, tmp_path):
        """Test that get_verse_path() handles double-digit chapters."""
        from src.data_writer import get_verse_path

        path = get_verse_path("Acts", 10, 44, tmp_path)

        assert "/10/" in str(path)

    def test_get_verse_path_formats_triple_digit_verse(self, tmp_path):
        """Test that get_verse_path() handles triple-digit verses (no padding for 3 digits)."""
        from src.data_writer import get_verse_path

        path = get_verse_path("Psalms", 119, 176, tmp_path)

        # Actually, we do zero-pad to 2 digits for consistency, but 176 is 3 digits
        # so it stays as 176
        assert path.name == "176.json"

    def test_write_verse_json_creates_file(self, tmp_path, sample_verse_data):
        """Test that write_verse_json() creates the file."""
        from src.data_writer import write_verse_json

        result = write_verse_json("Genesis", 1, 1, sample_verse_data, tmp_path)

        assert result is True

        # Check file exists
        expected_path = tmp_path / "data" / "OT" / "Genesis" / "01" / "01.json"
        assert expected_path.exists()

    def test_write_verse_json_creates_directories(self, tmp_path, sample_verse_data):
        """Test that write_verse_json() creates parent directories."""
        from src.data_writer import write_verse_json

        write_verse_json("Genesis", 1, 1, sample_verse_data, tmp_path)

        data_dir = tmp_path / "data" / "OT" / "Genesis" / "01"
        assert data_dir.exists()
        assert data_dir.is_dir()

    def test_write_verse_json_writes_correct_content(self, tmp_path, sample_verse_data):
        """Test that write_verse_json() writes correct JSON content."""
        from src.data_writer import write_verse_json

        write_verse_json("Genesis", 1, 1, sample_verse_data, tmp_path)

        expected_path = tmp_path / "data" / "OT" / "Genesis" / "01" / "01.json"
        with open(expected_path) as f:
            written_data = json.load(f)

        assert written_data == sample_verse_data

    def test_write_verse_json_pretty_prints(self, tmp_path, sample_verse_data):
        """Test that write_verse_json() pretty-prints JSON."""
        from src.data_writer import write_verse_json

        write_verse_json("Genesis", 1, 1, sample_verse_data, tmp_path)

        expected_path = tmp_path / "data" / "OT" / "Genesis" / "01" / "01.json"
        content = expected_path.read_text()

        # Check for indentation
        assert "\n" in content
        assert "  " in content or "\t" in content

    def test_write_verse_json_overwrites_existing(self, tmp_path, sample_verse_data):
        """Test that write_verse_json() overwrites existing files."""
        from src.data_writer import write_verse_json

        # Write first version
        write_verse_json("Genesis", 1, 1, sample_verse_data, tmp_path)

        # Write second version with different data
        modified_data = sample_verse_data.copy()
        modified_data["section_3_life_application"] = "Updated application"

        write_verse_json("Genesis", 1, 1, modified_data, tmp_path)

        # Check updated content
        expected_path = tmp_path / "data" / "OT" / "Genesis" / "01" / "01.json"
        with open(expected_path) as f:
            written_data = json.load(f)

        assert written_data["section_3_life_application"] == "Updated application"

    def test_atomic_write_creates_temp_file(self, tmp_path, sample_verse_data):
        """Test that atomic_write() uses a temporary file."""
        from src.data_writer import atomic_write

        target_path = tmp_path / "test.json"
        content = json.dumps(sample_verse_data)

        atomic_write(target_path, content)

        assert target_path.exists()

    def test_atomic_write_writes_content(self, tmp_path, sample_verse_data):
        """Test that atomic_write() writes correct content."""
        from src.data_writer import atomic_write

        target_path = tmp_path / "test.json"
        content = json.dumps(sample_verse_data)

        atomic_write(target_path, content)

        written_content = target_path.read_text()
        assert written_content == content

    def test_atomic_write_creates_parent_dirs(self, tmp_path, sample_verse_data):
        """Test that atomic_write() creates parent directories."""
        from src.data_writer import atomic_write

        target_path = tmp_path / "nested" / "dirs" / "test.json"
        content = json.dumps(sample_verse_data)

        atomic_write(target_path, content)

        assert target_path.exists()
        assert target_path.parent.exists()

    def test_verify_written_file_valid_json(self, tmp_path, sample_verse_data):
        """Test that verify_written_file() returns True for valid JSON."""
        from src.data_writer import verify_written_file

        file_path = tmp_path / "test.json"
        with open(file_path, 'w') as f:
            json.dump(sample_verse_data, f)

        result = verify_written_file(file_path, sample_verse_data)

        assert result is True

    def test_verify_written_file_invalid_json(self, tmp_path):
        """Test that verify_written_file() returns False for invalid JSON."""
        from src.data_writer import verify_written_file

        file_path = tmp_path / "test.json"
        file_path.write_text("Not valid JSON")

        result = verify_written_file(file_path, {"test": "data"})

        assert result is False

    def test_verify_written_file_missing_file(self, tmp_path):
        """Test that verify_written_file() returns False for missing file."""
        from src.data_writer import verify_written_file

        file_path = tmp_path / "nonexistent.json"

        result = verify_written_file(file_path, {"test": "data"})

        assert result is False

    def test_verify_written_file_mismatched_content(self, tmp_path):
        """Test that verify_written_file() returns False for mismatched content."""
        from src.data_writer import verify_written_file

        file_path = tmp_path / "test.json"
        with open(file_path, 'w') as f:
            json.dump({"original": "data"}, f)

        result = verify_written_file(file_path, {"different": "data"})

        assert result is False

    def test_write_verse_json_returns_false_on_error(self, tmp_path):
        """Test that write_verse_json() returns False on write error."""
        from src.data_writer import write_verse_json

        # Create a read-only directory to force write error
        readonly_dir = tmp_path / "readonly"
        readonly_dir.mkdir()
        readonly_dir.chmod(0o444)

        try:
            result = write_verse_json(
                "Genesis", 1, 1,
                {"test": "data"},
                readonly_dir
            )

            # Should return False due to permission error
            assert result is False
        finally:
            # Cleanup: restore write permissions
            readonly_dir.chmod(0o755)

    def test_get_testament_for_book_ot(self):
        """Test that get_testament_for_book() returns OT for Genesis."""
        from src.data_writer import get_testament_for_book

        assert get_testament_for_book("Genesis") == "OT"
        assert get_testament_for_book("Malachi") == "OT"

    def test_get_testament_for_book_nt(self):
        """Test that get_testament_for_book() returns NT for Acts."""
        from src.data_writer import get_testament_for_book

        assert get_testament_for_book("Acts") == "NT"
        assert get_testament_for_book("Revelation") == "NT"

    def test_get_testament_for_book_case_insensitive(self):
        """Test that get_testament_for_book() is case insensitive."""
        from src.data_writer import get_testament_for_book

        assert get_testament_for_book("genesis") == "OT"
        assert get_testament_for_book("ACTS") == "NT"

    def test_atomic_write_cleans_up_temp_on_error(self, tmp_path):
        """Test that atomic_write() cleans up temp file on error."""
        from src.data_writer import atomic_write
        from unittest.mock import patch

        target_path = tmp_path / "test.json"

        # Mock replace to raise an error after temp file is created
        with patch('pathlib.Path.replace', side_effect=OSError("Mock error")):
            result = atomic_write(target_path, "test content")

        assert result is False
        # Temp file should be cleaned up
        assert not (target_path.with_suffix('.tmp')).exists()

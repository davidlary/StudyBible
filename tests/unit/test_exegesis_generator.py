"""
Unit tests for exegesis_generator module.
Tests prompt building and exegesis generation orchestration.
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock


class TestExegesisGenerator:
    """Test suite for exegesis generation functionality."""

    @pytest.fixture
    def study_prompt_path(self):
        """Path to StudyPrompt.md file."""
        return Path(__file__).parent.parent.parent / "StudyPrompt.md"

    @pytest.fixture
    def mock_verse_text(self):
        """Mock verse text."""
        return "בְּרֵאשִׁית בָּרָא אֱלֹהִים"

    def test_load_study_prompt_returns_string(self, study_prompt_path):
        """Test that load_study_prompt() returns prompt text."""
        from src.exegesis_generator import load_study_prompt

        prompt = load_study_prompt(study_prompt_path)

        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_load_study_prompt_contains_key_phrases(self, study_prompt_path):
        """Test that loaded prompt contains expected key phrases."""
        from src.exegesis_generator import load_study_prompt

        prompt = load_study_prompt(study_prompt_path)

        assert "PRIMARY OBJECTIVE" in prompt
        assert "MANDATORY PRE-COMPUTATION GATE" in prompt
        assert "EXEGETICAL SYNTHESIS" in prompt

    def test_load_study_prompt_invalid_path_raises(self):
        """Test that load_study_prompt() raises for invalid path."""
        from src.exegesis_generator import load_study_prompt

        with pytest.raises((FileNotFoundError, IOError)):
            load_study_prompt(Path("/nonexistent/prompt.md"))

    def test_build_exegesis_prompt_returns_string(self, study_prompt_path, mock_verse_text):
        """Test that build_exegesis_prompt() returns a prompt string."""
        from src.exegesis_generator import build_exegesis_prompt

        prompt = build_exegesis_prompt(
            "Genesis", 1, 1, mock_verse_text, study_prompt_path
        )

        assert isinstance(prompt, str)
        assert len(prompt) > 0

    def test_build_exegesis_prompt_includes_verse_reference(
        self, study_prompt_path, mock_verse_text
    ):
        """Test that prompt includes verse reference."""
        from src.exegesis_generator import build_exegesis_prompt

        prompt = build_exegesis_prompt(
            "Genesis", 1, 1, mock_verse_text, study_prompt_path
        )

        assert "Genesis" in prompt
        assert "1:1" in prompt or "1" in prompt

    def test_build_exegesis_prompt_includes_original_text(
        self, study_prompt_path, mock_verse_text
    ):
        """Test that prompt includes original verse text."""
        from src.exegesis_generator import build_exegesis_prompt

        prompt = build_exegesis_prompt(
            "Genesis", 1, 1, mock_verse_text, study_prompt_path
        )

        assert mock_verse_text in prompt

    def test_build_exegesis_prompt_includes_study_instructions(
        self, study_prompt_path, mock_verse_text
    ):
        """Test that prompt includes study instructions."""
        from src.exegesis_generator import build_exegesis_prompt

        prompt = build_exegesis_prompt(
            "Genesis", 1, 1, mock_verse_text, study_prompt_path
        )

        assert "PRIMARY OBJECTIVE" in prompt or "exegetical" in prompt.lower()

    def test_build_exegesis_prompt_formats_verse_id(self, study_prompt_path, mock_verse_text):
        """Test that prompt formats verse ID correctly."""
        from src.exegesis_generator import build_exegesis_prompt

        prompt = build_exegesis_prompt(
            "Acts", 10, 44, mock_verse_text, study_prompt_path
        )

        assert "Acts" in prompt
        assert "10" in prompt
        assert "44" in prompt

    def test_generate_verse_exegesis_returns_dict(self, study_prompt_path):
        """Test that generate_verse_exegesis() returns a dictionary."""
        from src.exegesis_generator import generate_verse_exegesis

        mock_response = {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {},
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": ""
        }

        with patch('src.exegesis_generator.extract_verse', return_value="Hebrew text"):
            with patch('src.exegesis_generator.generate_exegesis', return_value=mock_response):
                result = generate_verse_exegesis(
                    "Genesis", 1, 1,
                    Path("/fake/oshb"),
                    Path("/fake/sblgnt"),
                    "fake_api_key",
                    study_prompt_path
                )

        assert isinstance(result, dict)
        assert "verse_id" in result

    def test_generate_verse_exegesis_calls_extract_verse(self, study_prompt_path):
        """Test that generate_verse_exegesis() calls extract_verse()."""
        from src.exegesis_generator import generate_verse_exegesis

        with patch('src.exegesis_generator.extract_verse', return_value="Hebrew text") as mock_extract:
            with patch('src.exegesis_generator.generate_exegesis', return_value={"verse_id": "GEN-1-1"}):
                generate_verse_exegesis(
                    "Genesis", 1, 1,
                    Path("/fake/oshb"),
                    Path("/fake/sblgnt"),
                    "fake_api_key",
                    study_prompt_path
                )

        mock_extract.assert_called_once()

    def test_generate_verse_exegesis_calls_generate_exegesis(self, study_prompt_path):
        """Test that generate_verse_exegesis() calls generate_exegesis()."""
        from src.exegesis_generator import generate_verse_exegesis

        with patch('src.exegesis_generator.extract_verse', return_value="Hebrew text"):
            with patch('src.exegesis_generator.generate_exegesis', return_value={"verse_id": "GEN-1-1"}) as mock_gen:
                generate_verse_exegesis(
                    "Genesis", 1, 1,
                    Path("/fake/oshb"),
                    Path("/fake/sblgnt"),
                    "fake_api_key",
                    study_prompt_path
                )

        mock_gen.assert_called_once()

    def test_generate_verse_exegesis_returns_none_if_extract_fails(self, study_prompt_path):
        """Test that generate_verse_exegesis() returns None if verse extraction fails."""
        from src.exegesis_generator import generate_verse_exegesis

        with patch('src.exegesis_generator.extract_verse', return_value=None):
            result = generate_verse_exegesis(
                "Genesis", 1, 1,
                Path("/fake/oshb"),
                Path("/fake/sblgnt"),
                "fake_api_key",
                study_prompt_path
            )

        assert result is None

    def test_generate_verse_exegesis_returns_none_if_api_fails(self, study_prompt_path):
        """Test that generate_verse_exegesis() returns None if API call fails."""
        from src.exegesis_generator import generate_verse_exegesis

        with patch('src.exegesis_generator.extract_verse', return_value="Hebrew text"):
            with patch('src.exegesis_generator.generate_exegesis', return_value=None):
                result = generate_verse_exegesis(
                    "Genesis", 1, 1,
                    Path("/fake/oshb"),
                    Path("/fake/sblgnt"),
                    "fake_api_key",
                    study_prompt_path
                )

        assert result is None

    def test_format_verse_reference_standard(self):
        """Test that format_verse_reference() formats standard references."""
        from src.exegesis_generator import format_verse_reference

        assert format_verse_reference("Genesis", 1, 1) == "Genesis 1:1"
        assert format_verse_reference("Acts", 10, 44) == "Acts 10:44"

    def test_format_verse_reference_handles_numbers(self):
        """Test that format_verse_reference() handles books with numbers."""
        from src.exegesis_generator import format_verse_reference

        assert format_verse_reference("1 Corinthians", 13, 1) == "1 Corinthians 13:1"
        assert format_verse_reference("2 Timothy", 3, 16) == "2 Timothy 3:16"

    def test_format_verse_id_standard(self):
        """Test that format_verse_id() formats standard IDs."""
        from src.exegesis_generator import format_verse_id

        assert format_verse_id("Genesis", 1, 1) == "GEN-1-1"
        assert format_verse_id("Acts", 10, 44) == "ACTS-10-44"

    def test_format_verse_id_handles_spaces(self):
        """Test that format_verse_id() removes spaces from book names."""
        from src.exegesis_generator import format_verse_id

        assert format_verse_id("1 Corinthians", 13, 1) == "1COR-13-1"
        assert format_verse_id("Song of Solomon", 2, 1) == "SONG-2-1"

    def test_format_verse_id_uppercase(self):
        """Test that format_verse_id() converts to uppercase."""
        from src.exegesis_generator import format_verse_id

        assert format_verse_id("genesis", 1, 1) == "GEN-1-1"
        assert format_verse_id("acts", 10, 44) == "ACTS-10-44"

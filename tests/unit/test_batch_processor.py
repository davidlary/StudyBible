"""
Unit tests for batch_processor module.
Tests batch processing of chapters with checkpointing.
"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock


class TestBatchProcessor:
    """Test suite for batch processing functionality."""

    @pytest.fixture
    def mock_config(self, tmp_path):
        """Mock configuration."""
        return {
            "base_path": tmp_path,
            "oshb_path": tmp_path / "morphhb",
            "sblgnt_path": tmp_path / "sblgnt",
            "api_key": "test_key",
            "study_prompt_path": tmp_path / "StudyPrompt.md"
        }

    def test_process_verse_returns_true_on_success(self, mock_config):
        """Test that process_verse() returns True on successful processing."""
        from src.batch_processor import process_verse

        with patch('src.batch_processor.generate_verse_exegesis', return_value={"verse_id": "GEN-1-1"}):
            with patch('src.batch_processor.validate_verse_json', return_value=True):
                with patch('src.batch_processor.write_verse_json', return_value=True):
                    result = process_verse("Genesis", 1, 1, mock_config)

        assert result is True

    def test_process_verse_returns_false_if_generation_fails(self, mock_config):
        """Test that process_verse() returns False if exegesis generation fails."""
        from src.batch_processor import process_verse

        with patch('src.batch_processor.generate_verse_exegesis', return_value=None):
            result = process_verse("Genesis", 1, 1, mock_config)

        assert result is False

    def test_process_verse_returns_false_if_validation_fails(self, mock_config):
        """Test that process_verse() returns False if validation fails."""
        from src.batch_processor import process_verse

        with patch('src.batch_processor.generate_verse_exegesis', return_value={"verse_id": "GEN-1-1"}):
            with patch('src.batch_processor.validate_verse_json', return_value=False):
                result = process_verse("Genesis", 1, 1, mock_config)

        assert result is False

    def test_process_verse_returns_false_if_write_fails(self, mock_config):
        """Test that process_verse() returns False if write fails."""
        from src.batch_processor import process_verse

        with patch('src.batch_processor.generate_verse_exegesis', return_value={"verse_id": "GEN-1-1"}):
            with patch('src.batch_processor.validate_verse_json', return_value=True):
                with patch('src.batch_processor.write_verse_json', return_value=False):
                    result = process_verse("Genesis", 1, 1, mock_config)

        assert result is False

    def test_process_chapter_returns_dict_with_results(self, mock_config):
        """Test that process_chapter() returns results dictionary."""
        from src.batch_processor import process_chapter

        with patch('src.batch_processor.get_verse_count', return_value=2):
            with patch('src.batch_processor.process_verse', return_value=True):
                result = process_chapter("Genesis", 1, mock_config)

        assert isinstance(result, dict)
        assert "total" in result
        assert "successful" in result
        assert "failed" in result

    def test_process_chapter_counts_successes(self, mock_config):
        """Test that process_chapter() counts successful verses."""
        from src.batch_processor import process_chapter

        with patch('src.batch_processor.get_verse_count', return_value=3):
            with patch('src.batch_processor.process_verse', return_value=True):
                result = process_chapter("Genesis", 1, mock_config)

        assert result["total"] == 3
        assert result["successful"] == 3
        assert result["failed"] == 0

    def test_process_chapter_counts_failures(self, mock_config):
        """Test that process_chapter() counts failed verses."""
        from src.batch_processor import process_chapter

        with patch('src.batch_processor.get_verse_count', return_value=3):
            with patch('src.batch_processor.process_verse', side_effect=[True, False, True]):
                result = process_chapter("Genesis", 1, mock_config)

        assert result["total"] == 3
        assert result["successful"] == 2
        assert result["failed"] == 1

    def test_create_checkpoint_writes_file(self, tmp_path):
        """Test that create_checkpoint() writes checkpoint file."""
        from src.batch_processor import create_checkpoint

        checkpoint_data = {"book": "Genesis", "chapter": 1, "verse": 5}

        create_checkpoint(checkpoint_data, tmp_path)

        checkpoint_file = tmp_path / ".checkpoint.json"
        assert checkpoint_file.exists()

    def test_create_checkpoint_writes_correct_data(self, tmp_path):
        """Test that create_checkpoint() writes correct data."""
        from src.batch_processor import create_checkpoint

        checkpoint_data = {"book": "Genesis", "chapter": 1, "verse": 5}

        create_checkpoint(checkpoint_data, tmp_path)

        checkpoint_file = tmp_path / ".checkpoint.json"
        with open(checkpoint_file) as f:
            written_data = json.load(f)

        assert written_data == checkpoint_data

    def test_load_checkpoint_returns_dict(self, tmp_path):
        """Test that load_checkpoint() returns checkpoint data."""
        from src.batch_processor import load_checkpoint, create_checkpoint

        checkpoint_data = {"book": "Genesis", "chapter": 1, "verse": 5}
        create_checkpoint(checkpoint_data, tmp_path)

        loaded_data = load_checkpoint(tmp_path)

        assert loaded_data == checkpoint_data

    def test_load_checkpoint_returns_none_if_missing(self, tmp_path):
        """Test that load_checkpoint() returns None if no checkpoint."""
        from src.batch_processor import load_checkpoint

        result = load_checkpoint(tmp_path)

        assert result is None

    def test_clear_checkpoint_removes_file(self, tmp_path):
        """Test that clear_checkpoint() removes checkpoint file."""
        from src.batch_processor import clear_checkpoint, create_checkpoint

        checkpoint_data = {"book": "Genesis", "chapter": 1}
        create_checkpoint(checkpoint_data, tmp_path)

        clear_checkpoint(tmp_path)

        checkpoint_file = tmp_path / ".checkpoint.json"
        assert not checkpoint_file.exists()

    def test_clear_checkpoint_handles_missing_file(self, tmp_path):
        """Test that clear_checkpoint() handles missing checkpoint gracefully."""
        from src.batch_processor import clear_checkpoint

        # Should not raise error
        clear_checkpoint(tmp_path)

    def test_process_chapter_creates_checkpoint(self, mock_config):
        """Test that process_chapter() creates checkpoint after each verse."""
        from src.batch_processor import process_chapter

        with patch('src.batch_processor.get_verse_count', return_value=2):
            with patch('src.batch_processor.process_verse', return_value=True):
                with patch('src.batch_processor.create_checkpoint') as mock_checkpoint:
                    process_chapter("Genesis", 1, mock_config)

        # Should create checkpoint for each verse
        assert mock_checkpoint.call_count >= 2

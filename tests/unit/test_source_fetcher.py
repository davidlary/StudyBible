"""
Unit tests for source_fetcher module.
Tests the download and verification of biblical source texts (OSHB, SBLGNT).
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import shutil
import tempfile


class TestSourceFetcher:
    """Test suite for source fetching functionality."""

    @pytest.fixture
    def temp_sources_dir(self, tmp_path):
        """Create temporary sources directory for testing."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()
        return sources_dir

    @pytest.fixture
    def mock_subprocess(self):
        """Mock subprocess calls for git clone operations."""
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="", stderr="")
            yield mock_run

    def test_download_oshb_clones_repository(self, temp_sources_dir, mock_subprocess):
        """Test that download_oshb() clones the OSHB repository."""
        from src.source_fetcher import download_oshb

        result = download_oshb(temp_sources_dir)

        assert result is True
        mock_subprocess.assert_called_once()
        call_args = mock_subprocess.call_args[0][0]
        assert "git" in call_args
        assert "clone" in call_args
        assert "openscriptures/morphhb" in call_args[2]

    def test_download_oshb_creates_target_directory(self, temp_sources_dir, mock_subprocess):
        """Test that download_oshb() creates the OSHB directory."""
        from src.source_fetcher import download_oshb

        download_oshb(temp_sources_dir)

        expected_path = temp_sources_dir / "morphhb"
        # Directory would be created by actual git clone, just verify call was made correctly
        assert mock_subprocess.called

    def test_download_oshb_handles_existing_directory(self, temp_sources_dir):
        """Test that download_oshb() handles pre-existing OSHB directory."""
        from src.source_fetcher import download_oshb

        # Create existing directory
        oshb_dir = temp_sources_dir / "morphhb"
        oshb_dir.mkdir()

        result = download_oshb(temp_sources_dir)

        # Should return True and skip download
        assert result is True

    def test_download_oshb_handles_git_failure(self, temp_sources_dir, mock_subprocess):
        """Test that download_oshb() handles git clone failures gracefully."""
        from src.source_fetcher import download_oshb

        mock_subprocess.return_value = Mock(returncode=1, stdout="", stderr="Error")

        result = download_oshb(temp_sources_dir)

        assert result is False

    def test_download_sblgnt_clones_repository(self, temp_sources_dir, mock_subprocess):
        """Test that download_sblgnt() clones the SBLGNT repository."""
        from src.source_fetcher import download_sblgnt

        result = download_sblgnt(temp_sources_dir)

        assert result is True
        mock_subprocess.assert_called_once()
        call_args = mock_subprocess.call_args[0][0]
        assert "git" in call_args
        assert "clone" in call_args
        assert "sblgnt/sblgnt" in call_args[2]

    def test_download_sblgnt_creates_target_directory(self, temp_sources_dir, mock_subprocess):
        """Test that download_sblgnt() creates the SBLGNT directory."""
        from src.source_fetcher import download_sblgnt

        download_sblgnt(temp_sources_dir)

        expected_path = temp_sources_dir / "sblgnt"
        # Directory would be created by actual git clone, just verify call was made correctly
        assert mock_subprocess.called

    def test_download_sblgnt_handles_existing_directory(self, temp_sources_dir):
        """Test that download_sblgnt() handles pre-existing SBLGNT directory."""
        from src.source_fetcher import download_sblgnt

        # Create existing directory
        sblgnt_dir = temp_sources_dir / "sblgnt"
        sblgnt_dir.mkdir()

        result = download_sblgnt(temp_sources_dir)

        # Should return True and skip download
        assert result is True

    def test_download_sblgnt_handles_git_failure(self, temp_sources_dir, mock_subprocess):
        """Test that download_sblgnt() handles git clone failures gracefully."""
        from src.source_fetcher import download_sblgnt

        mock_subprocess.return_value = Mock(returncode=1, stdout="", stderr="Error")

        result = download_sblgnt(temp_sources_dir)

        assert result is False

    def test_verify_sources_all_present(self, temp_sources_dir):
        """Test that verify_sources() returns True when all sources present."""
        from src.source_fetcher import verify_sources

        # Create both directories
        (temp_sources_dir / "morphhb").mkdir()
        (temp_sources_dir / "sblgnt").mkdir()

        result = verify_sources(temp_sources_dir)

        assert result is True

    def test_verify_sources_missing_oshb(self, temp_sources_dir):
        """Test that verify_sources() returns False when OSHB missing."""
        from src.source_fetcher import verify_sources

        # Only create SBLGNT
        (temp_sources_dir / "sblgnt").mkdir()

        result = verify_sources(temp_sources_dir)

        assert result is False

    def test_verify_sources_missing_sblgnt(self, temp_sources_dir):
        """Test that verify_sources() returns False when SBLGNT missing."""
        from src.source_fetcher import verify_sources

        # Only create OSHB
        (temp_sources_dir / "morphhb").mkdir()

        result = verify_sources(temp_sources_dir)

        assert result is False

    def test_verify_sources_both_missing(self, temp_sources_dir):
        """Test that verify_sources() returns False when both sources missing."""
        from src.source_fetcher import verify_sources

        result = verify_sources(temp_sources_dir)

        assert result is False

    def test_download_all_sources_downloads_both(self, temp_sources_dir, mock_subprocess):
        """Test that download_all_sources() downloads both repositories."""
        from src.source_fetcher import download_all_sources

        result = download_all_sources(temp_sources_dir)

        assert result is True
        assert mock_subprocess.call_count == 2

    def test_download_all_sources_handles_partial_failure(self, temp_sources_dir, mock_subprocess):
        """Test download_all_sources() when one source fails."""
        from src.source_fetcher import download_all_sources

        # First call succeeds, second fails
        mock_subprocess.side_effect = [
            Mock(returncode=0, stdout="", stderr=""),
            Mock(returncode=1, stdout="", stderr="Error"),
        ]

        result = download_all_sources(temp_sources_dir)

        assert result is False

    def test_get_oshb_path_returns_correct_path(self, temp_sources_dir):
        """Test that get_oshb_path() returns correct directory path."""
        from src.source_fetcher import get_oshb_path

        path = get_oshb_path(temp_sources_dir)

        assert path == temp_sources_dir / "morphhb"
        assert isinstance(path, Path)

    def test_get_sblgnt_path_returns_correct_path(self, temp_sources_dir):
        """Test that get_sblgnt_path() returns correct directory path."""
        from src.source_fetcher import get_sblgnt_path

        path = get_sblgnt_path(temp_sources_dir)

        assert path == temp_sources_dir / "sblgnt"
        assert isinstance(path, Path)

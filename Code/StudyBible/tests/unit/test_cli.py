"""
Unit tests for cli module.
Tests command-line interface functionality.
"""

import pytest
from click.testing import CliRunner
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path


class TestCLI:
    """Test suite for CLI functionality."""

    @pytest.fixture
    def runner(self):
        """Create CLI test runner."""
        return CliRunner()

    @pytest.fixture
    def mock_config(self):
        """Mock configuration."""
        return {
            "base_path": Path("/fake/path"),
            "oshb_path": Path("/fake/oshb"),
            "sblgnt_path": Path("/fake/sblgnt"),
            "api_key": "fake_key",
            "study_prompt_path": Path("/fake/prompt.md")
        }

    def test_cli_main_group_exists(self, runner):
        """Test that main CLI group exists."""
        from src.cli import cli

        result = runner.invoke(cli, ['--help'])

        assert result.exit_code == 0
        assert "Usage:" in result.output

    def test_cli_has_generate_command(self, runner):
        """Test that generate command exists."""
        from src.cli import cli

        result = runner.invoke(cli, ['generate', '--help'])

        assert result.exit_code == 0
        assert "generate" in result.output.lower()

    def test_cli_has_generate_chapter_command(self, runner):
        """Test that generate-chapter command exists."""
        from src.cli import cli

        result = runner.invoke(cli, ['generate-chapter', '--help'])

        assert result.exit_code == 0

    def test_cli_has_download_sources_command(self, runner):
        """Test that download-sources command exists."""
        from src.cli import cli

        result = runner.invoke(cli, ['download-sources', '--help'])

        assert result.exit_code == 0

    def test_generate_command_requires_book(self, runner):
        """Test that generate command requires book argument."""
        from src.cli import cli

        result = runner.invoke(cli, ['generate'])

        assert result.exit_code != 0

    def test_generate_command_requires_chapter(self, runner):
        """Test that generate command requires chapter argument."""
        from src.cli import cli

        result = runner.invoke(cli, ['generate', 'Genesis'])

        assert result.exit_code != 0

    def test_generate_command_requires_verse(self, runner):
        """Test that generate command requires verse argument."""
        from src.cli import cli

        result = runner.invoke(cli, ['generate', 'Genesis', '1'])

        assert result.exit_code != 0

    def test_generate_command_calls_process_verse(self, runner):
        """Test that generate command calls process_verse."""
        from src.cli import cli

        with patch('src.cli.load_config', return_value={}):
            with patch('src.cli.process_verse', return_value=True) as mock_process:
                result = runner.invoke(cli, ['generate', 'Genesis', '1', '1'])

        mock_process.assert_called_once()

    def test_generate_command_success_message(self, runner):
        """Test that generate command shows success message."""
        from src.cli import cli

        with patch('src.cli.load_config', return_value={}):
            with patch('src.cli.process_verse', return_value=True):
                result = runner.invoke(cli, ['generate', 'Genesis', '1', '1'])

        assert "success" in result.output.lower() or "generated" in result.output.lower()

    def test_generate_command_failure_message(self, runner):
        """Test that generate command shows failure message."""
        from src.cli import cli

        with patch('src.cli.load_config', return_value={}):
            with patch('src.cli.process_verse', return_value=False):
                result = runner.invoke(cli, ['generate', 'Genesis', '1', '1'])

        assert "fail" in result.output.lower() or "error" in result.output.lower()

    def test_generate_chapter_command_calls_process_chapter(self, runner):
        """Test that generate-chapter calls process_chapter."""
        from src.cli import cli

        results = {"total": 31, "successful": 31, "failed": 0}

        with patch('src.cli.load_config', return_value={}):
            with patch('src.cli.process_chapter', return_value=results) as mock_process:
                result = runner.invoke(cli, ['generate-chapter', 'Genesis', '1'])

        mock_process.assert_called_once()

    def test_generate_chapter_command_shows_results(self, runner):
        """Test that generate-chapter shows processing results."""
        from src.cli import cli

        results = {"total": 31, "successful": 30, "failed": 1}

        with patch('src.cli.load_config', return_value={}):
            with patch('src.cli.process_chapter', return_value=results):
                result = runner.invoke(cli, ['generate-chapter', 'Genesis', '1'])

        assert "30" in result.output or "31" in result.output

    def test_download_sources_command_calls_download_all(self, runner):
        """Test that download-sources calls download_all_sources."""
        from src.cli import cli

        with patch('src.cli.get_sources_directory', return_value=Path('/fake')):
            with patch('src.cli.download_all_sources', return_value=True) as mock_download:
                result = runner.invoke(cli, ['download-sources'])

        mock_download.assert_called_once()

    def test_download_sources_command_success_message(self, runner):
        """Test that download-sources shows success message."""
        from src.cli import cli

        with patch('src.cli.get_sources_directory', return_value=Path('/fake')):
            with patch('src.cli.download_all_sources', return_value=True):
                result = runner.invoke(cli, ['download-sources'])

        assert "success" in result.output.lower() or "download" in result.output.lower()

    def test_load_config_returns_dict(self):
        """Test that load_config returns a dictionary."""
        from src.cli import load_config

        with patch('src.cli.get_gemini_api_key', return_value="fake_key"):
            with patch('src.cli.get_project_root', return_value=Path('/fake')):
                with patch('src.cli.get_sources_directory', return_value=Path('/fake/sources')):
                    config = load_config()

        assert isinstance(config, dict)
        assert "api_key" in config

    def test_load_config_includes_all_required_keys(self):
        """Test that load_config includes all required configuration keys."""
        from src.cli import load_config

        with patch('src.cli.get_gemini_api_key', return_value="fake_key"):
            with patch('src.cli.get_project_root', return_value=Path('/fake')):
                with patch('src.cli.get_sources_directory', return_value=Path('/fake/sources')):
                    config = load_config()

        required_keys = ["base_path", "oshb_path", "sblgnt_path", "api_key", "study_prompt_path"]
        for key in required_keys:
            assert key in config

"""
Unit tests for src/config.py

Test-Driven Development: These tests define expected behavior BEFORE implementation.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
import os


@pytest.mark.unit
class TestConfig:
    """Test configuration management module"""

    def test_load_config_returns_dict(self):
        """Test that load_config returns a dictionary"""
        from src.config import load_config

        with patch.dict(os.environ, {"GOOGLE_API_KEY": "test_key_123"}):
            config = load_config()
            assert isinstance(config, dict)
            assert "gemini_api_key" in config
            assert "paths" in config

    def test_get_gemini_api_key_from_environment(self):
        """Test getting API key from environment variable"""
        from src.config import get_gemini_api_key

        with patch.dict(os.environ, {"GOOGLE_API_KEY": "AIzaSyTest123"}):
            api_key = get_gemini_api_key()
            assert api_key == "AIzaSyTest123"
            assert api_key.startswith("AIzaSy")

    def test_get_gemini_api_key_strips_prefix(self):
        """Test that API key prefix 'google_api_key: ' is stripped"""
        from src.config import get_gemini_api_key

        # Simulate the format from environment
        with patch.dict(os.environ, {"GOOGLE_API_KEY": "google_api_key: AIzaSyTest123"}):
            api_key = get_gemini_api_key()
            assert api_key == "AIzaSyTest123"
            assert not api_key.startswith("google_api_key:")

    def test_get_gemini_api_key_raises_when_missing(self):
        """Test that missing API key raises ValueError"""
        from src.config import get_gemini_api_key

        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
                get_gemini_api_key()

    def test_get_gemini_api_key_raises_when_empty(self):
        """Test that empty API key raises ValueError"""
        from src.config import get_gemini_api_key

        with patch.dict(os.environ, {"GOOGLE_API_KEY": ""}):
            with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
                get_gemini_api_key()

    def test_get_data_path_ot_book(self):
        """Test generating data path for Old Testament book"""
        from src.config import get_data_path

        path = get_data_path("OT", "Genesis", 1, 1)
        assert isinstance(path, Path)
        assert "data/OT/GEN/01/01.json" in str(path)

    def test_get_data_path_nt_book(self):
        """Test generating data path for New Testament book"""
        from src.config import get_data_path

        path = get_data_path("NT", "Acts", 10, 1)
        assert isinstance(path, Path)
        assert "data/NT/ACT/10/01.json" in str(path)

    def test_get_data_path_formats_correctly(self):
        """Test that chapter and verse are zero-padded correctly"""
        from src.config import get_data_path

        path = get_data_path("NT", "Matthew", 5, 3)
        path_str = str(path)
        assert "/05/" in path_str  # Chapter zero-padded
        assert "/03.json" in path_str  # Verse zero-padded

    def test_get_data_path_double_digit_chapter(self):
        """Test path with double-digit chapter number"""
        from src.config import get_data_path

        path = get_data_path("NT", "Acts", 10, 48)
        path_str = str(path)
        assert "/10/" in path_str  # Chapter 10
        assert "/48.json" in path_str  # Verse 48

    def test_validate_config_valid(self):
        """Test that valid configuration passes validation"""
        from src.config import validate_config

        with patch.dict(os.environ, {"GOOGLE_API_KEY": "AIzaSyTest123"}):
            is_valid, errors = validate_config()
            assert is_valid is True
            assert len(errors) == 0

    def test_validate_config_missing_api_key(self):
        """Test that missing API key fails validation"""
        from src.config import validate_config

        with patch.dict(os.environ, {}, clear=True):
            is_valid, errors = validate_config()
            assert is_valid is False
            assert len(errors) > 0
            assert any("API key" in str(err) for err in errors)

    def test_get_project_root(self):
        """Test getting project root directory"""
        from src.config import get_project_root

        root = get_project_root()
        assert isinstance(root, Path)
        assert root.exists()
        # Should contain src/ directory
        assert (root / "src").exists()

    def test_get_sources_directory(self):
        """Test getting sources directory path"""
        from src.config import get_sources_directory

        sources_dir = get_sources_directory()
        assert isinstance(sources_dir, Path)
        assert "sources" in str(sources_dir)

    def test_get_schemas_directory(self):
        """Test getting schemas directory path"""
        from src.config import get_schemas_directory

        schemas_dir = get_schemas_directory()
        assert isinstance(schemas_dir, Path)
        assert "schemas" in str(schemas_dir)

    def test_config_includes_model_settings(self):
        """Test that config includes Gemini model settings"""
        from src.config import load_config

        with patch.dict(os.environ, {"GOOGLE_API_KEY": "test_key"}):
            config = load_config()
            assert "gemini_model" in config
            assert "thinking" in config["gemini_model"].lower() or "gemini" in config["gemini_model"]

    def test_config_paths_are_absolute(self):
        """Test that all configuration paths are absolute"""
        from src.config import load_config

        with patch.dict(os.environ, {"GOOGLE_API_KEY": "test_key"}):
            config = load_config()
            paths = config["paths"]
            for key, path in paths.items():
                assert Path(path).is_absolute(), f"Path {key} should be absolute"

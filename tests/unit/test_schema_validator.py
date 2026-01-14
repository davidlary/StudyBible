"""
Unit tests for schema_validator module.
Tests JSON schema validation for biblical verse exegesis data.
"""

import pytest
import json
from pathlib import Path
from jsonschema import ValidationError


class TestSchemaValidator:
    """Test suite for schema validation functionality."""

    @pytest.fixture
    def schema_path(self):
        """Path to verse schema file."""
        return Path(__file__).parent.parent.parent / "schemas" / "verse_schema.json"

    @pytest.fixture
    def valid_verse_path(self):
        """Path to valid verse fixture."""
        return Path(__file__).parent.parent / "fixtures" / "valid_verse.json"

    @pytest.fixture
    def invalid_verse_missing_field_path(self):
        """Path to invalid verse fixture (missing fields)."""
        return Path(__file__).parent.parent / "fixtures" / "invalid_verse_missing_field.json"

    @pytest.fixture
    def invalid_verse_bad_coords_path(self):
        """Path to invalid verse fixture (bad coordinates)."""
        return Path(__file__).parent.parent / "fixtures" / "invalid_verse_bad_coordinates.json"

    def test_load_schema_returns_dict(self, schema_path):
        """Test that load_schema() returns a dictionary."""
        from src.schema_validator import load_schema

        schema = load_schema(schema_path)

        assert isinstance(schema, dict)
        assert "$schema" in schema or "type" in schema

    def test_load_schema_has_required_fields(self, schema_path):
        """Test that loaded schema has required top-level fields."""
        from src.schema_validator import load_schema

        schema = load_schema(schema_path)

        assert "type" in schema
        assert schema["type"] == "object"
        assert "properties" in schema
        assert "required" in schema

    def test_load_schema_invalid_path_raises(self):
        """Test that load_schema() raises for invalid path."""
        from src.schema_validator import load_schema

        with pytest.raises((FileNotFoundError, IOError)):
            load_schema(Path("/nonexistent/schema.json"))

    def test_validate_verse_json_valid_returns_true(self, schema_path, valid_verse_path):
        """Test that validate_verse_json() returns True for valid verse."""
        from src.schema_validator import validate_verse_json

        with open(valid_verse_path) as f:
            verse_data = json.load(f)

        result = validate_verse_json(verse_data, schema_path)

        assert result is True

    def test_validate_verse_json_missing_field_returns_false(
        self, schema_path, invalid_verse_missing_field_path
    ):
        """Test that validate_verse_json() returns False for missing required fields."""
        from src.schema_validator import validate_verse_json

        with open(invalid_verse_missing_field_path) as f:
            verse_data = json.load(f)

        result = validate_verse_json(verse_data, schema_path)

        assert result is False

    def test_validate_verse_json_bad_coordinates_returns_false(
        self, schema_path, invalid_verse_bad_coords_path
    ):
        """Test that validate_verse_json() returns False for invalid coordinates."""
        from src.schema_validator import validate_verse_json

        with open(invalid_verse_bad_coords_path) as f:
            verse_data = json.load(f)

        result = validate_verse_json(verse_data, schema_path)

        assert result is False

    def test_validate_verse_json_with_dict_schema(self, valid_verse_path):
        """Test validate_verse_json() accepts dict schema directly."""
        from src.schema_validator import validate_verse_json, load_schema

        schema_path = Path(__file__).parent.parent.parent / "schemas" / "verse_schema.json"
        schema = load_schema(schema_path)

        with open(valid_verse_path) as f:
            verse_data = json.load(f)

        result = validate_verse_json(verse_data, schema)

        assert result is True

    def test_validate_mandatory_fields_all_present(self, valid_verse_path):
        """Test that validate_mandatory_fields() passes for complete data."""
        from src.schema_validator import validate_mandatory_fields

        with open(valid_verse_path) as f:
            verse_data = json.load(f)

        result = validate_mandatory_fields(verse_data)

        assert result is True

    def test_validate_mandatory_fields_missing_verse_id(self):
        """Test that validate_mandatory_fields() fails without verse_id."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "section_1_sacred_text": {},
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_validate_mandatory_fields_missing_section_1(self):
        """Test that validate_mandatory_fields() fails without section_1."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "verse_id": "GEN-1-1",
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_validate_mandatory_fields_missing_original_script(self):
        """Test that validate_mandatory_fields() checks for original_script."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "faithful_direct_translation": "text",
                "standalone_english_translation": "text",
                "amplified_narrative_translation": "text",
            },
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_validate_mandatory_fields_empty_original_script(self):
        """Test that validate_mandatory_fields() rejects empty original_script."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "original_script": "",
                "faithful_direct_translation": "text",
                "standalone_english_translation": "text",
                "amplified_narrative_translation": "text",
            },
            "section_2_exegetical_synthesis": {},
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_validate_mandatory_fields_missing_dates(self):
        """Test that validate_mandatory_fields() checks historical dates."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "original_script": "text",
                "faithful_direct_translation": "text",
                "standalone_english_translation": "text",
                "amplified_narrative_translation": "text",
            },
            "section_2_exegetical_synthesis": {
                "historical_context_and_chronology": {
                    "context": "context text"
                }
            },
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_validate_mandatory_fields_missing_coordinates(self):
        """Test that validate_mandatory_fields() checks geospatial coordinates."""
        from src.schema_validator import validate_mandatory_fields

        verse_data = {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "original_script": "text",
                "faithful_direct_translation": "text",
                "standalone_english_translation": "text",
                "amplified_narrative_translation": "text",
            },
            "section_2_exegetical_synthesis": {
                "geospatial_and_physical_geography": {
                    "modern_location": "Place",
                    "altitude_m": 100,
                    "terrain_climate_characteristics": "terrain",
                }
            },
            "section_3_life_application": "text",
        }

        result = validate_mandatory_fields(verse_data)

        assert result is False

    def test_get_validation_errors_returns_list(self, schema_path, invalid_verse_missing_field_path):
        """Test that get_validation_errors() returns list of error messages."""
        from src.schema_validator import get_validation_errors

        with open(invalid_verse_missing_field_path) as f:
            verse_data = json.load(f)

        errors = get_validation_errors(verse_data, schema_path)

        assert isinstance(errors, list)
        assert len(errors) > 0
        assert all(isinstance(e, str) for e in errors)

    def test_get_validation_errors_valid_returns_empty(self, schema_path, valid_verse_path):
        """Test that get_validation_errors() returns empty list for valid data."""
        from src.schema_validator import get_validation_errors

        with open(valid_verse_path) as f:
            verse_data = json.load(f)

        errors = get_validation_errors(verse_data, schema_path)

        assert isinstance(errors, list)
        assert len(errors) == 0

    def test_validate_verse_id_format_valid(self):
        """Test that validate_verse_id_format() accepts valid IDs."""
        from src.schema_validator import validate_verse_id_format

        assert validate_verse_id_format("GEN-1-1") is True
        assert validate_verse_id_format("ACTS-10-44") is True
        assert validate_verse_id_format("REV-22-21") is True

    def test_validate_verse_id_format_invalid(self):
        """Test that validate_verse_id_format() rejects invalid IDs."""
        from src.schema_validator import validate_verse_id_format

        assert validate_verse_id_format("Genesis 1:1") is False
        assert validate_verse_id_format("GEN-1") is False
        assert validate_verse_id_format("invalid") is False

    def test_validate_coordinates_valid(self):
        """Test that validate_coordinates() accepts valid coordinates."""
        from src.schema_validator import validate_coordinates

        assert validate_coordinates(32.5, 35.5) is True
        assert validate_coordinates(0, 0) is True
        assert validate_coordinates(-90, 180) is True

    def test_validate_coordinates_invalid_lat(self):
        """Test that validate_coordinates() rejects invalid latitude."""
        from src.schema_validator import validate_coordinates

        assert validate_coordinates(100, 35.5) is False
        assert validate_coordinates(-100, 35.5) is False

    def test_validate_coordinates_invalid_long(self):
        """Test that validate_coordinates() rejects invalid longitude."""
        from src.schema_validator import validate_coordinates

        assert validate_coordinates(32.5, 200) is False
        assert validate_coordinates(32.5, -200) is False

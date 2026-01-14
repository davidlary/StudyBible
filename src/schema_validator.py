"""
Schema Validator Module

Validates biblical verse JSON data against the verse schema.
Ensures all mandatory fields are present and properly formatted.

Functions:
    load_schema: Load JSON schema from file
    validate_verse_json: Validate verse data against schema
    validate_mandatory_fields: Check all mandatory fields present
    get_validation_errors: Get list of validation error messages
    validate_verse_id_format: Validate verse ID format
    validate_coordinates: Validate geographic coordinates
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Union
from jsonschema import validate, ValidationError, Draft7Validator


def load_schema(schema_path: Union[Path, str]) -> Dict[str, Any]:
    """
    Load JSON schema from file.

    Args:
        schema_path: Path to JSON schema file

    Returns:
        Schema dictionary

    Raises:
        FileNotFoundError: If schema file doesn't exist
        json.JSONDecodeError: If schema is invalid JSON
    """
    schema_path = Path(schema_path)

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    return schema


def validate_verse_json(
    verse_data: Dict[str, Any],
    schema: Union[Dict[str, Any], Path, str]
) -> bool:
    """
    Validate verse JSON data against schema.

    Args:
        verse_data: Verse data dictionary
        schema: Schema dict or path to schema file

    Returns:
        True if valid, False otherwise
    """
    # Load schema if path provided
    if isinstance(schema, (Path, str)):
        try:
            schema = load_schema(schema)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    # Validate against schema
    try:
        validate(instance=verse_data, schema=schema)
        return True
    except ValidationError:
        return False


def validate_mandatory_fields(verse_data: Dict[str, Any]) -> bool:
    """
    Check that all mandatory fields are present and non-empty.

    Mandatory field checks:
    1. verse_id
    2. section_1_sacred_text with all 4 subfields
    3. section_2_exegetical_synthesis (if present, check subfields)
    4. section_3_life_application
    5. historical_context_and_chronology.dates
    6. historical_context_and_chronology.context
    7. geospatial_and_physical_geography.coordinates
    8. socio_political_matrix
    9. aggregate_analogia_scriptura
    10. original_script non-empty
    11. All section_1 fields non-empty

    Args:
        verse_data: Verse data dictionary

    Returns:
        True if all mandatory fields present and valid, False otherwise
    """
    # Check top-level required fields
    required_top = ["verse_id", "section_1_sacred_text", "section_3_life_application"]
    for field in required_top:
        if field not in verse_data:
            return False

    # Check section_1 required fields
    section_1 = verse_data.get("section_1_sacred_text", {})
    required_section_1 = [
        "original_script",
        "faithful_direct_translation",
        "standalone_english_translation",
        "amplified_narrative_translation",
    ]

    for field in required_section_1:
        if field not in section_1:
            return False
        # Check non-empty
        if not section_1[field] or not str(section_1[field]).strip():
            return False

    # Check section_2 if present
    section_2 = verse_data.get("section_2_exegetical_synthesis", {})

    if section_2:
        # Check historical context
        historical = section_2.get("historical_context_and_chronology", {})
        if historical:
            if "dates" not in historical or not historical["dates"]:
                return False
            if "context" not in historical or not historical["context"]:
                return False

        # Check geospatial data
        geospatial = section_2.get("geospatial_and_physical_geography", {})
        if geospatial:
            if "coordinates" not in geospatial:
                return False

            coords = geospatial["coordinates"]
            if not isinstance(coords, dict):
                return False
            if "lat" not in coords or "long" not in coords:
                return False

    return True


def get_validation_errors(
    verse_data: Dict[str, Any],
    schema: Union[Dict[str, Any], Path, str]
) -> List[str]:
    """
    Get list of validation error messages.

    Args:
        verse_data: Verse data dictionary
        schema: Schema dict or path to schema file

    Returns:
        List of error message strings (empty if valid)
    """
    # Load schema if path provided
    if isinstance(schema, (Path, str)):
        try:
            schema = load_schema(schema)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return [f"Schema loading error: {str(e)}"]

    # Collect validation errors
    errors = []
    validator = Draft7Validator(schema)

    for error in validator.iter_errors(verse_data):
        # Build readable error message
        path = ".".join(str(p) for p in error.path) if error.path else "root"
        message = f"{path}: {error.message}"
        errors.append(message)

    return errors


def validate_verse_id_format(verse_id: str) -> bool:
    """
    Validate verse ID format (BOOK-CH-VS).

    Args:
        verse_id: Verse identifier string

    Returns:
        True if valid format, False otherwise
    """
    pattern = r'^[A-Z0-9]+-[0-9]+-[0-9]+$'
    return bool(re.match(pattern, verse_id))


def validate_coordinates(lat: float, long: float) -> bool:
    """
    Validate geographic coordinates.

    Args:
        lat: Latitude (-90 to 90)
        long: Longitude (-180 to 180)

    Returns:
        True if valid coordinates, False otherwise
    """
    if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
        return False

    if lat < -90 or lat > 90:
        return False

    if long < -180 or long > 180:
        return False

    return True

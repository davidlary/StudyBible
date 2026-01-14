"""
Configuration Management for StudyBible

Handles API keys, paths, and settings for the exegesis generation system.
"""

import os
from pathlib import Path
from typing import Dict, Any, Tuple, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_project_root() -> Path:
    """
    Get the project root directory.

    Returns:
        Path: Absolute path to project root
    """
    # Assuming this file is in src/, project root is one level up
    return Path(__file__).parent.parent.absolute()


def get_gemini_api_key() -> str:
    """
    Get and validate Google Gemini API key from environment or YAML file.

    The key may be in format "google_api_key: 'ACTUAL_KEY'" which needs to be parsed.
    Falls back to reading directly from .env-keys.yml if environment variable is malformed.

    Returns:
        str: Valid Gemini API key

    Raises:
        ValueError: If API key is missing or empty
    """
    api_key = os.environ.get("GOOGLE_API_KEY", "").strip()

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable is missing or empty. "
            "Please set it with: export GOOGLE_API_KEY='your-key-here'"
        )

    # Handle format: "google_api_key: 'ACTUAL_KEY'" (with YAML syntax and quotes)
    if ":" in api_key and api_key.startswith("google_api_key"):
        api_key = api_key.split(":", 1)[1].strip()
        # Remove surrounding quotes if present
        if api_key.startswith("'") and api_key.endswith("'"):
            api_key = api_key[1:-1]
        elif api_key.startswith('"') and api_key.endswith('"'):
            api_key = api_key[1:-1]

    # If key still looks malformed or is old expired key, read directly from YAML
    if not api_key.startswith("AIzaSy") or "BArMBNvTzE" in api_key:
        logger.warning("Environment variable malformed or expired. Reading from YAML file.")
        yaml_path = Path.home() / "Dropbox" / "Environments" / ".env-keys.yml"
        if yaml_path.exists():
            with open(yaml_path, 'r') as f:
                for line in f:
                    if line.strip().startswith("google_api_key:"):
                        # Extract: google_api_key: 'AIza...'
                        api_key = line.split(":", 1)[1].strip()
                        # Remove quotes
                        if api_key.startswith("'") and api_key.endswith("'"):
                            api_key = api_key[1:-1]
                        elif api_key.startswith('"') and api_key.endswith('"'):
                            api_key = api_key[1:-1]
                        break
        else:
            raise ValueError(f"YAML file not found at {yaml_path}")

    if not api_key or not api_key.startswith("AIzaSy"):
        raise ValueError(
            "GOOGLE_API_KEY is empty or invalid after parsing. "
            "Please set a valid API key."
        )

    logger.info(f"API key loaded successfully (ends with: ...{api_key[-8:]})")
    return api_key


def get_sources_directory() -> Path:
    """
    Get the sources directory path where OSHB and SBLGNT are stored.

    Returns:
        Path: Absolute path to sources directory
    """
    return get_project_root() / "sources"


def get_schemas_directory() -> Path:
    """
    Get the schemas directory path where JSON schemas are stored.

    Returns:
        Path: Absolute path to schemas directory
    """
    return get_project_root() / "schemas"


def get_data_directory() -> Path:
    """
    Get the data directory path where generated JSON verses are stored.

    Returns:
        Path: Absolute path to data directory
    """
    return get_project_root() / "data"


def get_data_path(testament: str, book: str, chapter: int, verse: int) -> Path:
    """
    Generate file path for a specific verse JSON file.

    File structure: data/{OT|NT}/{BOOK_ABBR}/{CH}/{VS}.json
    Example: data/NT/ACT/10/01.json

    Args:
        testament: "OT" or "NT"
        book: Book name (e.g., "Genesis", "Acts")
        chapter: Chapter number
        verse: Verse number

    Returns:
        Path: Absolute path to verse JSON file
    """
    # Get book abbreviation (first 3 letters uppercase)
    book_abbr = book[:3].upper()

    # Zero-pad chapter and verse (2 digits)
    chapter_str = f"{chapter:02d}"
    verse_str = f"{verse:02d}"

    # Build path
    data_dir = get_data_directory()
    verse_path = data_dir / testament / book_abbr / chapter_str / f"{verse_str}.json"

    return verse_path


def load_config() -> Dict[str, Any]:
    """
    Load complete configuration for StudyBible system.

    Returns:
        Dict: Configuration dictionary with all settings

    Example:
        {
            "gemini_api_key": "AIzaSy...",
            "gemini_model": "gemini-2.0-flash-thinking-exp",
            "paths": {
                "root": Path(...),
                "sources": Path(...),
                "schemas": Path(...),
                "data": Path(...)
            },
            "rate_limit": {
                "requests_per_minute": 15,
                "delay_between_requests": 4
            }
        }
    """
    project_root = get_project_root()

    config = {
        "gemini_api_key": get_gemini_api_key(),
        "gemini_model": "gemini-2.0-flash-thinking-exp",  # Thinking mode model
        "gemini_model_fallback": "gemini-2.0-flash-exp",  # Fallback if thinking unavailable
        "paths": {
            "root": project_root,
            "sources": get_sources_directory(),
            "schemas": get_schemas_directory(),
            "data": get_data_directory(),
            "oshb": get_sources_directory() / "morphhb",
            "sblgnt": get_sources_directory() / "sblgnt",
        },
        "rate_limit": {
            "requests_per_minute": 15,  # Free tier limit
            "delay_between_requests": 4,  # Seconds
            "max_retries": 3,
            "backoff_multiplier": 2,
        },
        "generation": {
            "temperature": 0.7,
            "max_tokens": 8192,
            "timeout_seconds": 120,
        },
        "validation": {
            "schema_file": "verse_schema.json",
            "mandatory_checks": 11,
            "fail_on_missing_fields": True,
        },
        "checkpoint": {
            "enabled": True,
            "frequency_verses": 10,  # Checkpoint every 10 verses
            "checkpoint_dir": project_root / ".cpf" / "state",
        },
        "logging": {
            "level": "INFO",
            "log_dir": project_root / ".cpf" / "logs",
            "log_file": "studybible_operations.log",
        },
    }

    logger.info("Configuration loaded successfully")
    return config


def validate_config() -> Tuple[bool, List[str]]:
    """
    Validate configuration completeness and correctness.

    Returns:
        Tuple[bool, List[str]]: (is_valid, list_of_error_messages)
    """
    errors = []

    try:
        # Check API key
        api_key = get_gemini_api_key()
        if not api_key.startswith("AIzaSy"):
            errors.append("API key format appears invalid (should start with 'AIzaSy')")
    except ValueError as e:
        errors.append(f"API key validation failed: {str(e)}")

    # Check project structure
    project_root = get_project_root()
    required_dirs = ["src", "tests"]
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if not dir_path.exists():
            errors.append(f"Required directory missing: {dir_name}")

    # Check write permissions for data directory
    data_dir = get_data_directory()
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        errors.append(f"No write permission for data directory: {data_dir}")

    is_valid = len(errors) == 0

    if is_valid:
        logger.info("Configuration validation passed")
    else:
        logger.error(f"Configuration validation failed with {len(errors)} errors")
        for error in errors:
            logger.error(f"  - {error}")

    return is_valid, errors


# Auto-validate on import (can be disabled for testing)
if __name__ != "__main__":
    try:
        is_valid, errors = validate_config()
        if not is_valid:
            logger.warning("Configuration has issues but proceeding. Fix them before generation.")
    except Exception as e:
        logger.warning(f"Configuration validation skipped due to: {e}")

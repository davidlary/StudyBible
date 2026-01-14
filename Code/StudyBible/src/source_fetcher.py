"""
Source Fetcher Module

Downloads and manages biblical source texts:
- OSHB (Open Scriptures Hebrew Bible): https://github.com/openscriptures/morphhb
- SBLGNT (Society of Biblical Literature Greek New Testament): https://github.com/sblgnt/sblgnt

Functions:
    download_oshb: Clone the OSHB repository
    download_sblgnt: Clone the SBLGNT repository
    verify_sources: Check if both sources are present
    download_all_sources: Download both repositories
    get_oshb_path: Get path to OSHB directory
    get_sblgnt_path: Get path to SBLGNT directory
"""

import subprocess
from pathlib import Path
from typing import Optional


# Repository URLs
OSHB_REPO_URL = "https://github.com/openscriptures/morphhb.git"
SBLGNT_REPO_URL = "https://github.com/sblgnt/sblgnt.git"

# Directory names
OSHB_DIR_NAME = "morphhb"
SBLGNT_DIR_NAME = "sblgnt"


def download_oshb(sources_dir: Path) -> bool:
    """
    Download the OSHB (Open Scriptures Hebrew Bible) repository.

    Args:
        sources_dir: Directory where sources should be stored

    Returns:
        True if download successful or already exists, False otherwise
    """
    target_path = sources_dir / OSHB_DIR_NAME

    # Skip if already exists
    if target_path.exists() and target_path.is_dir():
        return True

    try:
        # Ensure parent directory exists
        sources_dir.mkdir(parents=True, exist_ok=True)

        # Clone repository
        result = subprocess.run(
            ["git", "clone", OSHB_REPO_URL, str(target_path)],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
        )

        return result.returncode == 0

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError) as e:
        return False


def download_sblgnt(sources_dir: Path) -> bool:
    """
    Download the SBLGNT (SBL Greek New Testament) repository.

    Args:
        sources_dir: Directory where sources should be stored

    Returns:
        True if download successful or already exists, False otherwise
    """
    target_path = sources_dir / SBLGNT_DIR_NAME

    # Skip if already exists
    if target_path.exists() and target_path.is_dir():
        return True

    try:
        # Ensure parent directory exists
        sources_dir.mkdir(parents=True, exist_ok=True)

        # Clone repository
        result = subprocess.run(
            ["git", "clone", SBLGNT_REPO_URL, str(target_path)],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
        )

        return result.returncode == 0

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError) as e:
        return False


def verify_sources(sources_dir: Path) -> bool:
    """
    Verify that both source repositories are present.

    Args:
        sources_dir: Directory where sources should be stored

    Returns:
        True if both OSHB and SBLGNT are present, False otherwise
    """
    oshb_path = sources_dir / OSHB_DIR_NAME
    sblgnt_path = sources_dir / SBLGNT_DIR_NAME

    return (
        oshb_path.exists()
        and oshb_path.is_dir()
        and sblgnt_path.exists()
        and sblgnt_path.is_dir()
    )


def download_all_sources(sources_dir: Path) -> bool:
    """
    Download both OSHB and SBLGNT repositories.

    Args:
        sources_dir: Directory where sources should be stored

    Returns:
        True if both downloads successful, False if any failed
    """
    oshb_success = download_oshb(sources_dir)
    sblgnt_success = download_sblgnt(sources_dir)

    return oshb_success and sblgnt_success


def get_oshb_path(sources_dir: Path) -> Path:
    """
    Get the path to the OSHB directory.

    Args:
        sources_dir: Base sources directory

    Returns:
        Path to OSHB directory
    """
    return sources_dir / OSHB_DIR_NAME


def get_sblgnt_path(sources_dir: Path) -> Path:
    """
    Get the path to the SBLGNT directory.

    Args:
        sources_dir: Base sources directory

    Returns:
        Path to SBLGNT directory
    """
    return sources_dir / SBLGNT_DIR_NAME

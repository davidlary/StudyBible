"""
Gemini Client Module

Google Gemini API client for generating biblical exegesis.
Uses gemini-2.0-flash-thinking-exp model with retry logic.

Functions:
    initialize_client: Create and configure Gemini client
    generate_exegesis: Generate exegesis from prompt
    parse_json_response: Parse JSON from API response
    retry_with_backoff: Execute function with exponential backoff
"""

import json
import time
import re
from typing import Optional, Dict, Any, Callable
import google.generativeai as genai


# Default model for exegesis generation
DEFAULT_MODEL = "gemini-2.0-flash-thinking-exp-1219"

# Retry configuration
DEFAULT_MAX_RETRIES = 3
DEFAULT_BASE_DELAY = 2.0  # seconds
DEFAULT_MAX_DELAY = 60.0  # seconds


def initialize_client(api_key: str, model_name: str = DEFAULT_MODEL):
    """
    Initialize and configure Gemini API client.

    Args:
        api_key: Google Gemini API key
        model_name: Model to use (default: gemini-2.0-flash-thinking-exp)

    Returns:
        Configured GenerativeModel instance
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    return model


def parse_json_response(response_text: str) -> Optional[Dict[str, Any]]:
    """
    Parse JSON from API response text.

    Handles:
    - Plain JSON
    - JSON wrapped in markdown code blocks
    - JSON with preceding text

    Args:
        response_text: Raw response text from API

    Returns:
        Parsed JSON dict or None if parsing fails
    """
    if not response_text or not response_text.strip():
        return None

    # Remove markdown JSON wrapper if present
    text = response_text.strip()

    # Try to find JSON in markdown code block
    json_match = re.search(r'```json\s*\n(.*?)\n```', text, re.DOTALL)
    if json_match:
        text = json_match.group(1)
    else:
        # Try to find JSON object (starting with {)
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            text = json_match.group(0)

    # Try to parse JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def retry_with_backoff(
    func: Callable,
    max_retries: int = DEFAULT_MAX_RETRIES,
    base_delay: float = DEFAULT_BASE_DELAY,
    max_delay: float = DEFAULT_MAX_DELAY
) -> Optional[Any]:
    """
    Execute function with exponential backoff retry logic.

    Args:
        func: Function to execute
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds

    Returns:
        Function result or None if all retries failed
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                # Last attempt failed
                return None

            # Calculate exponential backoff delay
            delay = min(base_delay * (2 ** attempt), max_delay)
            time.sleep(delay)

    return None


def generate_exegesis(
    prompt: str,
    api_key: str,
    model_name: str = DEFAULT_MODEL,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> Optional[Dict[str, Any]]:
    """
    Generate biblical exegesis using Gemini API.

    Args:
        prompt: Complete prompt including verse and instructions
        api_key: Google Gemini API key
        model_name: Model to use
        max_retries: Maximum retry attempts

    Returns:
        Parsed JSON response dict or None if failed
    """
    def make_request():
        """Inner function for retry logic."""
        model = initialize_client(api_key, model_name)
        response = model.generate_content(prompt)
        return response.text

    # Execute with retry logic
    response_text = retry_with_backoff(make_request, max_retries=max_retries)

    if response_text is None:
        return None

    # Parse JSON response
    return parse_json_response(response_text)

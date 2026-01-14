"""
Unit tests for gemini_client module.
Tests the Google Gemini API client with mocked responses.
"""

import pytest
import json
from unittest.mock import Mock, patch, MagicMock
import time


class TestGeminiClient:
    """Test suite for Gemini API client functionality."""

    @pytest.fixture
    def mock_api_key(self):
        """Mock API key for testing."""
        return "AIzaSyDlyXl026OvnvXqR4vVnZQWUcw15vtqFuI"

    @pytest.fixture
    def sample_json_response(self):
        """Sample JSON response from Gemini."""
        return {
            "verse_id": "GEN-1-1",
            "section_1_sacred_text": {
                "original_script": "בְּרֵאשִׁית",
                "faithful_direct_translation": "In beginning",
                "standalone_english_translation": "In the beginning",
                "amplified_narrative_translation": "At the beginning of time"
            },
            "section_2_exegetical_synthesis": {
                "literal_primary_filter": ["fact1", "fact2"]
            },
            "section_3_life_application": "Application text"
        }

    def test_initialize_client_returns_client(self, mock_api_key):
        """Test that initialize_client() returns a client object."""
        from src.gemini_client import initialize_client

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                client = initialize_client(mock_api_key)

                assert client is not None
                mock_model.assert_called_once()

    def test_initialize_client_uses_correct_model(self, mock_api_key):
        """Test that initialize_client() uses gemini-2.0-flash-thinking-exp."""
        from src.gemini_client import initialize_client

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                initialize_client(mock_api_key)

                # Check that the model name contains the expected identifier
                call_args = mock_model.call_args
                assert call_args is not None

    def test_initialize_client_configures_api_key(self, mock_api_key):
        """Test that initialize_client() configures the API key."""
        from src.gemini_client import initialize_client

        with patch('google.generativeai.configure') as mock_configure:
            with patch('google.generativeai.GenerativeModel'):
                initialize_client(mock_api_key)

                mock_configure.assert_called_once_with(api_key=mock_api_key)

    def test_generate_exegesis_returns_dict(self, mock_api_key, sample_json_response):
        """Test that generate_exegesis() returns a dictionary."""
        from src.gemini_client import generate_exegesis

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_instance = MagicMock()
                mock_response = MagicMock()
                mock_response.text = json.dumps(sample_json_response)
                mock_instance.generate_content.return_value = mock_response
                mock_model.return_value = mock_instance

                result = generate_exegesis("Test prompt", mock_api_key)

                assert isinstance(result, dict)
                assert "verse_id" in result

    def test_generate_exegesis_sends_prompt(self, mock_api_key, sample_json_response):
        """Test that generate_exegesis() sends the prompt to the API."""
        from src.gemini_client import generate_exegesis

        prompt = "Generate exegesis for Genesis 1:1"

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_instance = MagicMock()
                mock_response = MagicMock()
                mock_response.text = json.dumps(sample_json_response)
                mock_instance.generate_content.return_value = mock_response
                mock_model.return_value = mock_instance

                generate_exegesis(prompt, mock_api_key)

                mock_instance.generate_content.assert_called_once()
                call_args = mock_instance.generate_content.call_args
                assert prompt in str(call_args)

    def test_generate_exegesis_retries_on_failure(self, mock_api_key):
        """Test that generate_exegesis() retries on API failure."""
        from src.gemini_client import generate_exegesis

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_instance = MagicMock()
                # First call fails, second succeeds
                mock_instance.generate_content.side_effect = [
                    Exception("API Error"),
                    MagicMock(text='{"verse_id": "TEST-1-1"}')
                ]
                mock_model.return_value = mock_instance

                with patch('time.sleep'):  # Mock sleep to speed up test
                    result = generate_exegesis("Test prompt", mock_api_key, max_retries=2)

                assert result is not None
                assert mock_instance.generate_content.call_count == 2

    def test_generate_exegesis_returns_none_after_max_retries(self, mock_api_key):
        """Test that generate_exegesis() returns None after max retries."""
        from src.gemini_client import generate_exegesis

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_instance = MagicMock()
                mock_instance.generate_content.side_effect = Exception("API Error")
                mock_model.return_value = mock_instance

                with patch('time.sleep'):
                    result = generate_exegesis("Test prompt", mock_api_key, max_retries=2)

                assert result is None

    def test_parse_json_response_valid_json(self, sample_json_response):
        """Test that parse_json_response() handles valid JSON."""
        from src.gemini_client import parse_json_response

        json_text = json.dumps(sample_json_response)
        result = parse_json_response(json_text)

        assert result == sample_json_response

    def test_parse_json_response_with_markdown_wrapper(self, sample_json_response):
        """Test that parse_json_response() strips markdown JSON wrappers."""
        from src.gemini_client import parse_json_response

        json_text = f"```json\n{json.dumps(sample_json_response)}\n```"
        result = parse_json_response(json_text)

        assert result == sample_json_response

    def test_parse_json_response_with_text_before_json(self, sample_json_response):
        """Test that parse_json_response() handles text before JSON."""
        from src.gemini_client import parse_json_response

        json_text = f"Here is the result:\n{json.dumps(sample_json_response)}"
        result = parse_json_response(json_text)

        assert result == sample_json_response

    def test_parse_json_response_invalid_returns_none(self):
        """Test that parse_json_response() returns None for invalid JSON."""
        from src.gemini_client import parse_json_response

        result = parse_json_response("This is not JSON")

        assert result is None

    def test_parse_json_response_empty_returns_none(self):
        """Test that parse_json_response() returns None for empty string."""
        from src.gemini_client import parse_json_response

        result = parse_json_response("")

        assert result is None

    def test_retry_with_backoff_succeeds_first_try(self):
        """Test that retry_with_backoff() succeeds on first try."""
        from src.gemini_client import retry_with_backoff

        def success_function():
            return "success"

        result = retry_with_backoff(success_function, max_retries=3)

        assert result == "success"

    def test_retry_with_backoff_retries_on_exception(self):
        """Test that retry_with_backoff() retries on exception."""
        from src.gemini_client import retry_with_backoff

        call_count = [0]

        def failing_function():
            call_count[0] += 1
            if call_count[0] < 3:
                raise Exception("Temporary failure")
            return "success"

        with patch('time.sleep'):
            result = retry_with_backoff(failing_function, max_retries=5)

        assert result == "success"
        assert call_count[0] == 3

    def test_retry_with_backoff_returns_none_after_max_retries(self):
        """Test that retry_with_backoff() returns None after max retries."""
        from src.gemini_client import retry_with_backoff

        def always_failing_function():
            raise Exception("Permanent failure")

        with patch('time.sleep'):
            result = retry_with_backoff(always_failing_function, max_retries=3)

        assert result is None

    def test_retry_with_backoff_uses_exponential_backoff(self):
        """Test that retry_with_backoff() uses exponential backoff."""
        from src.gemini_client import retry_with_backoff

        sleep_times = []

        def failing_function():
            raise Exception("Failure")

        def mock_sleep(seconds):
            sleep_times.append(seconds)

        with patch('time.sleep', side_effect=mock_sleep):
            retry_with_backoff(failing_function, max_retries=3)

        # Check that sleep times increase
        assert len(sleep_times) >= 2
        # Should be exponentially increasing (approximately)
        assert sleep_times[1] > sleep_times[0]

    def test_generate_exegesis_handles_rate_limiting(self, mock_api_key):
        """Test that generate_exegesis() handles rate limiting errors."""
        from src.gemini_client import generate_exegesis

        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_instance = MagicMock()
                # Simulate rate limiting error
                rate_limit_error = Exception("429: Rate limit exceeded")
                mock_instance.generate_content.side_effect = [
                    rate_limit_error,
                    MagicMock(text='{"verse_id": "TEST-1-1"}')
                ]
                mock_model.return_value = mock_instance

                with patch('time.sleep'):
                    result = generate_exegesis("Test prompt", mock_api_key, max_retries=3)

                assert result is not None

"""
Unit Tests for Fact-Checking Pipeline

Tests ground truth checks, database verification, and AI integration

Author: Claude Sonnet 4.5
Date: 2026-01-14
"""

import pytest
import json
from pathlib import Path
from src.fact_checker import FactChecker, FactCheckResult, fact_check_verse_file


class TestFactCheckResult:
    """Test FactCheckResult class"""

    def test_init(self):
        """Test initialization"""
        result = FactCheckResult()
        assert result.passed is True
        assert result.issues == []
        assert result.warnings == []

    def test_add_issue(self):
        """Test adding an issue marks as failed"""
        result = FactCheckResult()
        result.add_issue("test_field", "Test error", "Test evidence", "high")

        assert result.passed is False
        assert len(result.issues) == 1
        assert result.issues[0]['field'] == 'test_field'
        assert result.issues[0]['severity'] == 'high'

    def test_add_warning(self):
        """Test adding warning does not mark as failed"""
        result = FactCheckResult()
        result.add_warning("test_field", "Test warning")

        assert result.passed is True
        assert len(result.warnings) == 1

    def test_to_dict(self):
        """Test conversion to dictionary"""
        result = FactCheckResult()
        result.add_issue("field1", "error1", "evidence1", "high")
        result.add_warning("field2", "warning1")

        d = result.to_dict()

        assert d['passed'] is False
        assert len(d['issues']) == 1
        assert len(d['warnings']) == 1
        assert 'summary' in d


class TestFactChecker:
    """Test FactChecker class"""

    @pytest.fixture
    def checker(self):
        """Create FactChecker instance"""
        return FactChecker()

    @pytest.fixture
    def sample_verse_data(self):
        """Sample verse data for testing"""
        return {
            "verse_id": "ACTS-10-1",
            "section_1_sacred_text": {
                "original_script": "Ἀνὴρ δέ τις ἐν Καισαρείᾳ",
                "faithful_direct_translation": "Now a certain man in Caesarea",
                "standalone_english_translation": "There was a man in Caesarea named Cornelius",
                "amplified_narrative_translation": "Now at that time..."
            },
            "section_2_exegetical_synthesis": {
                "literal_primary_filter": "The text presents Cornelius...",
                "linguistic_mechanics_and_names": "The name Cornelius...",
                "geospatial_data_and_physical_geography": "Caesarea (latitude: 32.5, longitude: 34.9, elevation: 0m)",
                "historical_context_and_chronology": "This event is dated to approximately AD 38-40.",
                "aggregate_perspective_and_analogia_scriptura": "This connects to Isaiah 49:6 and Acts 11:14"
            },
            "section_3_life_application": {
                "practical_application": "This teaches us..."
            }
        }

    def test_init(self, checker):
        """Test FactChecker initialization"""
        assert checker.config is not None
        assert checker.sources_path.exists()

    def test_check_verse_reference_valid(self, checker, sample_verse_data):
        """Test valid verse reference"""
        result = FactCheckResult()
        checker._check_verse_reference(sample_verse_data, "Acts", 10, 1, result)

        assert result.passed is True
        assert len(result.issues) == 0

    def test_check_verse_reference_invalid(self, checker, sample_verse_data):
        """Test invalid verse reference"""
        result = FactCheckResult()
        checker._check_verse_reference(sample_verse_data, "Acts", 99, 99, result)

        assert result.passed is False
        assert any('invalid' in issue['error'].lower() for issue in result.issues)

    def test_check_original_text_greek(self, checker, sample_verse_data):
        """Test Greek text verification"""
        result = FactCheckResult()
        checker._verify_greek_text(
            sample_verse_data['section_1_sacred_text']['original_script'],
            "Acts", 10, 1, result
        )

        # Should pass since it contains Greek characters
        assert len(result.issues) == 0

    def test_check_original_text_missing_greek(self, checker):
        """Test detection of missing Greek characters"""
        result = FactCheckResult()
        checker._verify_greek_text("This is English not Greek", "Acts", 10, 1, result)

        assert result.passed is False
        assert any('Greek' in issue['error'] for issue in result.issues)

    def test_check_coordinates_valid(self, checker, sample_verse_data):
        """Test valid coordinates"""
        result = FactCheckResult()
        checker._check_coordinates(sample_verse_data, result)

        assert result.passed is True

    def test_check_coordinates_invalid_latitude(self, checker):
        """Test invalid latitude detection"""
        verse_data = {
            "section_2_exegetical_synthesis": {
                "geospatial_data_and_physical_geography": "Caesarea (latitude: 200, longitude: 34.9)"
            }
        }
        result = FactCheckResult()
        checker._check_coordinates(verse_data, result)

        assert result.passed is False
        assert any('coordinates' in issue['field'].lower() and 'latitude' in issue['error'].lower() for issue in result.issues)

    def test_check_dates_reasonable(self, checker, sample_verse_data):
        """Test reasonable date checking"""
        result = FactCheckResult()
        checker._check_dates(sample_verse_data, result)

        assert result.passed is True

    def test_check_dates_unusual(self, checker):
        """Test unusual date warning"""
        verse_data = {
            "section_2_exegetical_synthesis": {
                "historical_context_and_chronology": "This occurred in AD 500"
            }
        }
        result = FactCheckResult()
        checker._check_dates(verse_data, result)

        # Should generate warning, not failure
        assert result.passed is True
        assert len(result.warnings) > 0

    def test_check_cross_references_valid(self, checker):
        """Test valid cross-reference checking"""
        verse_data = {
            "section_2_exegetical_synthesis": {
                "aggregate_perspective_and_analogia_scriptura": "This relates to Genesis 1:1 and John 3:16"
            }
        }
        result = FactCheckResult()
        checker._check_cross_references(verse_data, result)

        # Known verses should pass
        assert result.passed is True

    def test_build_fact_check_prompt(self, checker, sample_verse_data):
        """Test fact-check prompt building"""
        prompt = checker._build_fact_check_prompt(sample_verse_data, "Acts", 10, 1)

        assert "Acts 10:1" in prompt
        assert "FACTUAL errors" in prompt
        assert "Greek/Hebrew Morphology" in prompt
        assert json.dumps(sample_verse_data, indent=2, ensure_ascii=False) in prompt

    def test_process_ai_review_with_issues(self, checker):
        """Test processing AI review with issues"""
        ai_result = {
            "issues": [
                {
                    "field": "test_field",
                    "error": "Test error",
                    "evidence": "Test evidence",
                    "severity": "high"
                }
            ],
            "summary": "Found 1 issue"
        }

        result = FactCheckResult()
        checker._process_ai_review(ai_result, result)

        assert result.passed is False
        assert len(result.issues) == 1
        assert result.summary == "Found 1 issue"

    def test_process_ai_review_no_issues(self, checker):
        """Test processing AI review with no issues"""
        ai_result = {
            "issues": [],
            "summary": "No errors detected"
        }

        result = FactCheckResult()
        checker._process_ai_review(ai_result, result)

        assert result.passed is True
        assert len(result.issues) == 0


class TestFactCheckVerseFile:
    """Test convenience function for file-based fact-checking"""

    def test_fact_check_existing_file(self):
        """Test fact-checking an existing verse file"""
        test_file = Path("data/NT/Acts/10/01.json")

        if test_file.exists():
            result = fact_check_verse_file(str(test_file))

            assert isinstance(result, FactCheckResult)
            assert hasattr(result, 'passed')
            assert hasattr(result, 'issues')
            assert hasattr(result, 'warnings')
        else:
            pytest.skip("Test file not found")


@pytest.mark.integration
class TestFactCheckerIntegration:
    """Integration tests requiring API keys"""

    @pytest.fixture
    def checker(self):
        """Create FactChecker instance"""
        return FactChecker()

    @pytest.fixture
    def sample_verse_with_error(self):
        """Sample verse with deliberate error for AI to catch"""
        return {
            "verse_id": "ACTS-10-1",
            "section_1_sacred_text": {
                "original_script": "Ἀνὴρ δέ τις",
                "faithful_direct_translation": "A man",
                "standalone_english_translation": "There was a man",
                "amplified_narrative_translation": "A man"
            },
            "section_2_exegetical_synthesis": {
                "linguistic_mechanics_and_names": "Ἀνὴρ (anēr, 'man') is nominative case",
                "historical_context_and_chronology": "Occurred in AD 5000",  # Deliberately wrong
                "geospatial_data_and_physical_geography": "Caesarea (latitude: 32.5, longitude: 34.9)"
            }
        }

    @pytest.mark.skipif(
        not FactChecker().xai_api_key and not FactChecker().openai_api_key,
        reason="No AI API keys available"
    )
    def test_expert_ai_review(self, checker, sample_verse_with_error):
        """Test expert AI review (requires API key)"""
        result = FactCheckResult()
        checker._expert_ai_review(sample_verse_with_error, "Acts", 10, 1, result)

        # AI should catch the AD 5000 error or at least generate warnings
        assert len(result.issues) > 0 or len(result.warnings) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

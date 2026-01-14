"""
Fact-Checking Pipeline for StudyBible Verse Generation

Multi-tier verification system:
1. Ground truth checks (vs. source texts)
2. Database verification (coordinates, dates)
3. Expert AI review (Grok API)

Author: Claude Sonnet 4.5
Date: 2026-01-14
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import requests
from src.config import load_config, get_data_path
from src.bible_structure import validate_verse_reference


class FactCheckResult:
    """Result of fact-checking a verse"""

    def __init__(self):
        self.passed = True
        self.issues = []
        self.warnings = []
        self.summary = ""

    def add_issue(self, field: str, error: str, evidence: str, severity: str = "high"):
        """Add a factual error"""
        self.passed = False
        self.issues.append({
            "field": field,
            "error": error,
            "evidence": evidence,
            "severity": severity
        })

    def add_warning(self, field: str, message: str):
        """Add a non-critical warning"""
        self.warnings.append({
            "field": field,
            "message": message
        })

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "passed": self.passed,
            "issues": self.issues,
            "warnings": self.warnings,
            "summary": self.summary or f"Found {len(self.issues)} issues, {len(self.warnings)} warnings"
        }


class FactChecker:
    """Multi-tier fact-checking system for verse analysis"""

    def __init__(self):
        self.config = load_config()
        self.xai_api_key = os.getenv('XAI_API_KEY', '').replace('xai_api_key: ', '')
        self.openai_api_key = os.getenv('OPENAI_API_KEY', '').replace('openai_api_key: ', '')

        # Load source text paths
        self.sources_path = Path(__file__).parent.parent / "sources"
        self.sblgnt_path = self.sources_path / "sblgnt"
        self.oshb_path = self.sources_path / "morphhb"

    def check_verse(self, verse_data: Dict, book: str, chapter: int, verse: int) -> FactCheckResult:
        """
        Main fact-checking pipeline

        Args:
            verse_data: Generated verse JSON
            book: Book abbreviation (e.g., 'Acts')
            chapter: Chapter number
            verse: Verse number

        Returns:
            FactCheckResult object
        """
        result = FactCheckResult()

        # TIER 1: Ground truth checks
        self._check_verse_reference(verse_data, book, chapter, verse, result)
        self._check_original_text(verse_data, book, chapter, verse, result)
        self._check_cross_references(verse_data, result)

        # TIER 2: Database verification
        self._check_coordinates(verse_data, result)
        self._check_dates(verse_data, result)

        # TIER 3: Expert AI review (only if Tier 1 & 2 pass)
        if result.passed or len(result.issues) <= 2:
            self._expert_ai_review(verse_data, book, chapter, verse, result)

        return result

    def _check_verse_reference(self, verse_data: Dict, book: str, chapter: int, verse: int, result: FactCheckResult):
        """Verify verse reference is valid"""
        try:
            if not validate_verse_reference(book, chapter, verse):
                result.add_issue(
                    "verse_id",
                    f"Invalid verse reference: {book} {chapter}:{verse}",
                    "Verse does not exist in biblical canon",
                    "critical"
                )
        except Exception as e:
            result.add_warning("verse_id", f"Could not validate reference: {str(e)}")

    def _check_original_text(self, verse_data: Dict, book: str, chapter: int, verse: int, result: FactCheckResult):
        """
        Compare generated Greek/Hebrew text to source files

        For NT: Check against SBLGNT
        For OT: Check against OSHB
        """
        try:
            original_script = verse_data.get('section_1_sacred_text', {}).get('original_script', '')

            if not original_script:
                result.add_warning("original_script", "No original language text found")
                return

            # Determine testament
            from src.bible_structure import get_book_info
            book_info = get_book_info(book)

            if book_info and book_info['testament'] == 'NT':
                self._verify_greek_text(original_script, book, chapter, verse, result)
            else:
                self._verify_hebrew_text(original_script, book, chapter, verse, result)

        except Exception as e:
            result.add_warning("original_text", f"Could not verify original text: {str(e)}")

    def _verify_greek_text(self, generated_text: str, book: str, chapter: int, verse: int, result: FactCheckResult):
        """Verify Greek text against SBLGNT source"""
        # TODO: Implement SBLGNT text extraction
        # For now, just check that it contains Greek characters
        if not re.search(r'[\u0370-\u03FF]', generated_text):
            result.add_issue(
                "original_script",
                "Generated text does not contain Greek characters",
                "Expected Koine Greek for NT verse",
                "critical"
            )

    def _verify_hebrew_text(self, generated_text: str, book: str, chapter: int, verse: int, result: FactCheckResult):
        """Verify Hebrew/Aramaic text against OSHB source"""
        # TODO: Implement OSHB text extraction
        # For now, just check that it contains Hebrew characters
        if not re.search(r'[\u0590-\u05FF]', generated_text):
            result.add_issue(
                "original_script",
                "Generated text does not contain Hebrew characters",
                "Expected Biblical Hebrew/Aramaic for OT verse",
                "critical"
            )

    def _check_cross_references(self, verse_data: Dict, result: FactCheckResult):
        """Verify that cross-referenced verses exist"""
        try:
            exegesis = verse_data.get('section_2_exegetical_synthesis', {})

            # Check analogia scriptura field
            analogia = exegesis.get('aggregate_perspective_and_analogia_scriptura', '')
            if isinstance(analogia, list):
                analogia = ' '.join(analogia)

            # Extract verse references (e.g., "Genesis 1:1", "Acts 10:1-5")
            refs = re.findall(r'\b([1-3]?\s?[A-Z][a-z]+)\s+(\d+):(\d+(?:-\d+)?)\b', analogia)

            for book, chapter, verse_range in refs:
                book = book.strip()
                chapter_num = int(chapter)

                # Handle verse ranges (e.g., "1-5")
                if '-' in verse_range:
                    start, end = verse_range.split('-')
                    verse_num = int(start)
                else:
                    verse_num = int(verse_range)

                if not validate_verse_reference(book, chapter_num, verse_num):
                    result.add_issue(
                        "cross_references",
                        f"Invalid cross-reference: {book} {chapter}:{verse_range}",
                        "Referenced verse does not exist",
                        "medium"
                    )
        except Exception as e:
            result.add_warning("cross_references", f"Could not verify cross-references: {str(e)}")

    def _check_coordinates(self, verse_data: Dict, result: FactCheckResult):
        """Verify geographic coordinates are reasonable"""
        try:
            exegesis = verse_data.get('section_2_exegetical_synthesis', {})
            geo_data = exegesis.get('geospatial_data_and_physical_geography', '')

            if isinstance(geo_data, list):
                geo_data = ' '.join(geo_data)

            # Extract coordinate patterns
            # Latitude: -90 to 90, Longitude: -180 to 180
            lat_matches = re.findall(r'latitude[:\s]+(-?\d+\.?\d*)', geo_data, re.IGNORECASE)
            lon_matches = re.findall(r'longitude[:\s]+(-?\d+\.?\d*)', geo_data, re.IGNORECASE)

            for lat in lat_matches:
                lat_val = float(lat)
                if not (-90 <= lat_val <= 90):
                    result.add_issue(
                        "coordinates",
                        f"Invalid latitude: {lat_val}",
                        "Latitude must be between -90 and 90",
                        "high"
                    )

            for lon in lon_matches:
                lon_val = float(lon)
                if not (-180 <= lon_val <= 180):
                    result.add_issue(
                        "coordinates",
                        f"Invalid longitude: {lon_val}",
                        "Longitude must be between -180 and 180",
                        "high"
                    )
        except Exception as e:
            result.add_warning("coordinates", f"Could not verify coordinates: {str(e)}")

    def _check_dates(self, verse_data: Dict, result: FactCheckResult):
        """Verify historical dates are plausible"""
        try:
            exegesis = verse_data.get('section_2_exegetical_synthesis', {})
            historical = exegesis.get('historical_context_and_chronology', '')

            if isinstance(historical, list):
                historical = ' '.join(historical)

            # Extract AD/BC dates
            ad_dates = re.findall(r'AD\s+(\d+)', historical)
            bc_dates = re.findall(r'BC\s+(\d+)', historical)

            for date in ad_dates:
                year = int(date)
                if year < 1 or year > 150:  # Biblical events range
                    result.add_warning(
                        "dates",
                        f"Unusual AD date: {year} (biblical events typically 1-150 AD)"
                    )

            for date in bc_dates:
                year = int(date)
                if year > 4000:  # Creation to Christ
                    result.add_warning(
                        "dates",
                        f"Unusual BC date: {year} (biblical history typically < 4000 BC)"
                    )
        except Exception as e:
            result.add_warning("dates", f"Could not verify dates: {str(e)}")

    def _expert_ai_review(self, verse_data: Dict, book: str, chapter: int, verse: int, result: FactCheckResult):
        """
        Expert AI review using Grok API (primary) or OpenAI (fallback)

        Reviews:
        - Interlinear morphology accuracy
        - Etymology correctness
        - Historical claims
        - Geographic calculations
        - Cross-reference relevance
        """
        try:
            # Build fact-check prompt
            prompt = self._build_fact_check_prompt(verse_data, book, chapter, verse)

            # Try Grok API first
            ai_result = self._call_grok_api(prompt)

            if not ai_result:
                # Fallback to OpenAI
                ai_result = self._call_openai_api(prompt)

            if ai_result:
                self._process_ai_review(ai_result, result)
            else:
                result.add_warning("expert_review", "Could not complete AI fact-check (API unavailable)")

        except Exception as e:
            result.add_warning("expert_review", f"Expert AI review failed: {str(e)}")

    def _build_fact_check_prompt(self, verse_data: Dict, book: str, chapter: int, verse: int) -> str:
        """Build comprehensive fact-checking prompt"""
        verse_json = json.dumps(verse_data, indent=2, ensure_ascii=False)

        return f"""You are an expert biblical scholar specializing in Koine Greek, Biblical Hebrew, and biblical geography.

TASK: Review this AI-generated verse analysis for FACTUAL errors only.

VERSE: {book} {chapter}:{verse}

IGNORE:
- Theological interpretation (subjective)
- Stylistic choices
- Level of detail
- Application sections

FOCUS ON FACTUAL ACCURACY:
1. **Greek/Hebrew Morphology**: Are parsing codes correct (e.g., N-NSM, V-PAI-3S)?
2. **Etymology**: Are word origins accurate? Cite sources if correcting.
3. **Historical Facts**: Are dates, events, people correctly described?
4. **Geographic Data**: Are coordinates, distances, elevations reasonable?
5. **Cross-References**: Are biblical allusions/parallels legitimate?
6. **Original Language Formatting**: Should be "English (OriginalScript, transliteration)"
7. **Travel Time Calculations**: Are estimates reasonable for ancient travel?

VERSE ANALYSIS:
{verse_json}

OUTPUT FORMAT (JSON only, no other text):
{{
  "issues": [
    {{
      "field": "path.to.field",
      "error": "Description of error",
      "evidence": "Why this is wrong",
      "severity": "critical|high|medium|low"
    }}
  ],
  "summary": "Brief summary of findings"
}}

If NO issues found, return: {{"issues": [], "summary": "No factual errors detected"}}

Be rigorous but fair. Only report clear factual errors with evidence."""

    def _call_grok_api(self, prompt: str) -> Optional[Dict]:
        """Call xAI Grok API for fact-checking"""
        if not self.xai_api_key:
            return None

        try:
            url = "https://api.x.ai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.xai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "grok-beta",
                "messages": [
                    {"role": "system", "content": "You are a biblical fact-checker. Respond ONLY with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.1,  # Low temperature for factual accuracy
                "max_tokens": 2000
            }

            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()

            result = response.json()
            content = result['choices'][0]['message']['content']

            # Extract JSON from response (may be wrapped in markdown)
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))

            return None

        except Exception as e:
            print(f"Grok API error: {e}")
            return None

    def _call_openai_api(self, prompt: str) -> Optional[Dict]:
        """Fallback to OpenAI GPT-4 for fact-checking"""
        if not self.openai_api_key:
            return None

        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "gpt-4-turbo-preview",
                "messages": [
                    {"role": "system", "content": "You are a biblical fact-checker. Respond ONLY with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.1,
                "max_tokens": 2000,
                "response_format": {"type": "json_object"}
            }

            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()

            result = response.json()
            content = result['choices'][0]['message']['content']

            return json.loads(content)

        except Exception as e:
            print(f"OpenAI API error: {e}")
            return None

    def _process_ai_review(self, ai_result: Dict, result: FactCheckResult):
        """Process AI review results and add to fact-check result"""
        issues = ai_result.get('issues', [])

        for issue in issues:
            severity = issue.get('severity', 'medium')

            if severity in ['critical', 'high']:
                result.add_issue(
                    issue.get('field', 'unknown'),
                    issue.get('error', 'Unknown error'),
                    issue.get('evidence', 'See AI review'),
                    severity
                )
            else:
                result.add_warning(
                    issue.get('field', 'unknown'),
                    f"{issue.get('error', 'Unknown issue')}: {issue.get('evidence', '')}"
                )

        result.summary = ai_result.get('summary', result.summary)


def fact_check_verse_file(verse_file_path: str) -> FactCheckResult:
    """
    Convenience function to fact-check a verse JSON file

    Args:
        verse_file_path: Path to verse JSON file (e.g., data/NT/Acts/10/01.json)

    Returns:
        FactCheckResult object
    """
    # Extract book, chapter, verse from path
    path_parts = Path(verse_file_path).parts
    testament = path_parts[-4]  # NT or OT
    book = path_parts[-3]
    chapter = int(path_parts[-2])
    verse = int(Path(path_parts[-1]).stem)  # Remove .json

    # Load verse data
    with open(verse_file_path, 'r', encoding='utf-8') as f:
        verse_data = json.load(f)

    # Run fact-check
    checker = FactChecker()
    return checker.check_verse(verse_data, book, chapter, verse)


if __name__ == "__main__":
    # Test with Acts 10:25
    test_file = "data/NT/Acts/10/25.json"
    if Path(test_file).exists():
        print(f"Fact-checking {test_file}...")
        result = fact_check_verse_file(test_file)
        print(json.dumps(result.to_dict(), indent=2))
    else:
        print(f"Test file not found: {test_file}")

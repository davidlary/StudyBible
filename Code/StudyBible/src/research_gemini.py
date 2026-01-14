#!/usr/bin/env python3
"""
Deep research using Google Gemini API
Researches: Gemini models, Biblical manuscripts, Python testing frameworks
"""

import os
import json
import google.generativeai as genai
from datetime import datetime

def setup_gemini():
    """Configure Gemini API with key from environment"""
    api_key = os.environ.get('GOOGLE_API_KEY', '')
    # Handle format "google_api_key: ACTUAL_KEY"
    if ':' in api_key:
        api_key = api_key.split(':', 1)[1].strip()

    genai.configure(api_key=api_key)
    return api_key

def research_with_gemini(prompt, model_name='gemini-2.0-flash-thinking-exp'):
    """
    Use Gemini to conduct deep research

    Args:
        prompt: Research question/prompt
        model_name: Gemini model to use

    Returns:
        Research findings as text
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error with {model_name}: {e}")
        # Fallback to standard model
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e2:
            print(f"Error with fallback model: {e2}")
            return f"ERROR: {str(e2)}"

def main():
    """Conduct all research tasks"""
    print("=" * 80)
    print("DEEP RESEARCH USING GOOGLE GEMINI API")
    print("=" * 80)
    print()

    # Setup
    api_key = setup_gemini()
    print(f"✓ API Key configured (ends with: ...{api_key[-8:]})")
    print()

    research_results = {}

    # Research 1: Best Gemini Model
    print("[1/3] Researching: Best Gemini experimental thinking model for biblical exegesis")
    print("-" * 80)

    prompt_1 = """You are a technical AI consultant. Research and recommend the BEST Google Gemini experimental thinking model (as of January 2025) for deep biblical exegesis tasks that require:

1. Deep reasoning and multi-step logical analysis
2. Understanding of ancient languages (Hebrew, Greek)
3. Cross-referencing thousands of verses
4. Theological synthesis across entire biblical canon
5. Historical and archaeological context integration

Provide:
- Model name (exact API identifier)
- Key capabilities relevant to biblical scholarship
- Performance characteristics (context window, thinking depth, reasoning quality)
- Any limitations or considerations
- Recommended configuration parameters

Be specific and technical. Focus on CURRENT available models."""

    result_1 = research_with_gemini(prompt_1)
    research_results['gemini_model'] = result_1
    print(result_1)
    print()

    # Research 2: Biblical Manuscripts
    print("[2/3] Researching: Most reliable Hebrew/Greek biblical manuscripts")
    print("-" * 80)

    prompt_2 = """You are a biblical textual criticism expert. Provide a comprehensive analysis of the MOST RELIABLE Hebrew and Greek manuscript sources for creating a high-fidelity Bible translation.

For HEBREW OLD TESTAMENT, evaluate:
- Biblia Hebraica Stuttgartensia (BHS)
- Westminster Leningrad Codex (WLC)
- Leningrad Codex
- Aleppo Codex
- Dead Sea Scrolls integration
- Masoretic Text tradition

For GREEK NEW TESTAMENT, evaluate:
- Nestle-Aland 28th edition (NA28) / 30th edition (NA30)
- SBL Greek New Testament (SBLGNT)
- United Bible Societies Greek New Testament (UBS5)
- Textus Receptus
- Byzantine Majority Text

Provide:
1. HIGHEST FIDELITY recommendation for each testament
2. Manuscript age, provenance, scholarly consensus
3. Digital availability (machine-readable format)
4. API or dataset access methods
5. Practical considerations for programmatic access

Focus on ACCURACY and SCHOLARLY CONSENSUS. We need the best available source text."""

    result_2 = research_with_gemini(prompt_2)
    research_results['manuscripts'] = result_2
    print(result_2)
    print()

    # Research 3: Python Testing Framework
    print("[3/3] Researching: Best Python testing framework for robust validation")
    print("-" * 80)

    prompt_3 = """You are a Python software engineering expert. Recommend the BEST Python testing framework for a mission-critical biblical text processing system with these requirements:

Requirements:
1. Comprehensive unit testing with 80%+ coverage
2. Zero tolerance for silent failures
3. Detailed test reporting and logging
4. Easy integration with CI/CD (GitHub Actions)
5. Parameterized testing (testing 31,102 verses)
6. Fixtures for complex test data
7. Parallel test execution for performance
8. Clear assertion messages for debugging
9. Integration testing support
10. JSON schema validation testing

Evaluate:
- pytest (with plugins)
- unittest (standard library)
- nose2
- hypothesis (property-based testing)
- Other relevant frameworks

Provide:
1. PRIMARY recommendation with justification
2. Essential plugins/extensions needed
3. Configuration best practices
4. Coverage tools integration
5. Reporting and CI/CD integration
6. Example test structure

Be specific and practical. Focus on ROBUSTNESS and MAINTAINABILITY."""

    result_3 = research_with_gemini(prompt_3)
    research_results['testing_framework'] = result_3
    print(result_3)
    print()

    # Save results
    output_file = '/Users/davidlary/Dropbox/Environments/Code/StudyBible/.cpf/logs/gemini_research_results.json'
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'research': research_results
        }, f, indent=2)

    print("=" * 80)
    print(f"✓ Research complete! Results saved to: {output_file}")
    print("=" * 80)

    return research_results

if __name__ == '__main__':
    main()

# StudyBible

High-fidelity biblical exegesis with original language analysis, comprehensive theological synthesis, and AI-powered deep reasoning.

## Overview

StudyBible is a Python CLI application that generates comprehensive biblical exegesis for all 31,102 verses of the Protestant canon (66 books). Each verse includes:

- **Original Language Texts**: Hebrew (Westminster Leningrad Codex via OSHB) and Greek (SBLGNT)
- **Four Translations**: Original script, faithful direct translation, standalone English, amplified narrative
- **Exegetical Synthesis**: Ten comprehensive analysis dimensions including:
  - Literal-Primary Filter (Sensus Literalis)
  - Analogia Scriptura (Scripture interprets Scripture)
  - Philological & Grammatical Mechanics
  - Spatio-Temporal & Archaeological Matrix
  - Historical & Socio-Political Context
  - And more...
- **Life Application**: Practical guidance for contemporary living

## Features

- **AI-Powered Analysis**: Uses Google Gemini 2.5 Pro for deep reasoning and exegetical synthesis
- **Original Source Texts**: Direct extraction from OSHB (Hebrew) and SBLGNT (Greek) repositories
- **JSON Flat-File Database**: Structured data storage at `/data/{OT|NT}/{BOOK}/{CH}/{VS}.json`
- **Static Website**: Eleventy-powered site with full-text search via Pagefind
- **GitHub Pages Deployment**: Automatic deployment via GitHub Actions
- **Comprehensive Testing**: 190 tests with 81% coverage, pytest-based test suite

## Live Website

Visit the live StudyBible at: **https://davidlary.github.io/StudyBible/**

Currently available: **Acts Chapter 10** (all 48 verses with complete exegesis)

## Installation

### Prerequisites

- Python 3.12+
- Node.js 20+
- Google Gemini API key
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/davidlary/StudyBible.git
   cd StudyBible
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

4. **Download source texts:**
   ```bash
   python -m src.cli download-sources
   ```

5. **Install Node dependencies (for website):**
   ```bash
   npm install
   ```

## Usage

### Generate Single Verse

```bash
export GOOGLE_API_KEY="your_api_key_here"
python -m src.cli generate Acts 10 1
```

### Generate Entire Chapter

```bash
python -m src.cli generate-chapter Acts 10
```

### Build Website

```bash
npx eleventy
# Output in _site/ directory
```

### Run Tests

```bash
pytest                          # Run all tests
pytest --cov=src               # With coverage report
pytest tests/unit/              # Unit tests only
```

## Project Structure

```
StudyBible/
├── src/                        # Python source code
│   ├── config.py              # Configuration management
│   ├── bible_structure.py     # 66-book canon structure
│   ├── source_fetcher.py      # Download OSHB/SBLGNT
│   ├── verse_extractor.py     # Extract Hebrew/Greek text
│   ├── schema_validator.py    # JSON schema validation
│   ├── gemini_client.py       # Gemini API client
│   ├── exegesis_generator.py  # Orchestrate generation
│   ├── data_writer.py         # Write JSON files
│   ├── batch_processor.py     # Process multiple verses
│   └── cli.py                 # Command-line interface
├── tests/                     # Test suite (190 tests)
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test fixtures
├── data/                      # Generated verse JSON files
│   ├── NT/Acts/10/            # Acts chapter 10 (48 verses)
│   └── ...                    # Future chapters/books
├── sources/                   # Biblical source texts
│   ├── morphhb/               # OSHB (Hebrew)
│   └── sblgnt/                # SBLGNT (Greek)
├── website/                   # Eleventy static site
│   ├── _includes/             # Layout templates
│   ├── _data/                 # Data files
│   └── acts/                  # Acts chapter pages
├── schemas/                   # JSON validation schemas
│   └── verse_schema.json      # 58-field verse schema
├── StudyPrompt.md             # Exegetical requirements
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Technology Stack

### Backend
- **Python 3.12**: Core application
- **Google Gemini 2.5 Pro**: AI-powered exegetical analysis
- **pytest**: Testing framework (80%+ coverage)
- **lxml**: XML parsing (OSHB)
- **jsonschema**: JSON validation
- **click**: CLI framework
- **rich**: Beautiful terminal output

### Frontend
- **Eleventy (11ty)**: Static site generator
- **Pagefind**: Client-side search
- **Nunjucks**: Templating engine

### Sources
- **OSHB**: Open Scriptures Hebrew Bible (Westminster Leningrad Codex)
- **SBLGNT**: Society of Biblical Literature Greek New Testament

### Deployment
- **GitHub Pages**: Static hosting
- **GitHub Actions**: CI/CD pipeline

## Development

### Running Tests

```bash
# All tests with coverage
pytest --cov=src --cov-report=html

# Specific test file
pytest tests/unit/test_exegesis_generator.py -v

# Parallel execution (faster)
pytest -n auto
```

### Code Quality

```bash
# Linting
ruff check src/

# Type checking
mypy src/

# Formatting
black src/ tests/
```

## Architecture

### Generation Pipeline

1. **Extract Verse**: Read Hebrew/Greek text from source repositories
2. **Build Prompt**: Combine StudyPrompt.md with verse reference and text
3. **Generate Exegesis**: Call Gemini 2.5 Pro API with comprehensive prompt
4. **Validate JSON**: Check against 58-field schema with 11 mandatory validations
5. **Write File**: Atomic write to `/data/{testament}/{book}/{chapter}/{verse}.json`

### Website Build

1. **Data Loading**: Read JSON files from `/data` directory
2. **Template Rendering**: Nunjucks templates with verse data
3. **Static Generation**: Eleventy builds HTML pages
4. **Search Indexing**: Pagefind indexes all content
5. **Deployment**: GitHub Actions pushes to `gh-pages` branch

## API Usage

### Cost Estimation

- **Per Verse**: ~10-15KB input + ~5-10KB output = ~$0.01-0.02 per verse
- **Acts 10** (48 verses): ~$0.50-1.00
- **Full Bible** (31,102 verses): ~$300-600

### Rate Limits

- **Free Tier**: ~15 requests/minute
- **Estimated Time**:
  - Acts 10: 2-3 hours (48 verses)
  - Full Bible: 7-10 days (31,102 verses)

## Contributing

This is a personal research project. Contributions welcome via issues and pull requests.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Acknowledgments

- **OSHB**: Open Scriptures Hebrew Bible project
- **SBLGNT**: Society of Biblical Literature and Logos Bible Software
- **Google**: Gemini API for AI-powered analysis
- **Eleventy**: Excellent static site generator
- **CPF**: Context-Preserving Framework v4.3.0

## Contact

David Lary - [GitHub](https://github.com/davidlary)

Project Link: [https://github.com/davidlary/StudyBible](https://github.com/davidlary/StudyBible)

Website: [https://davidlary.github.io/StudyBible/](https://davidlary.github.io/StudyBible/)

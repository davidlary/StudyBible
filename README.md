# StudyBible

High-fidelity biblical exegesis with original language analysis, comprehensive theological synthesis, and AI-powered deep reasoning.

## Overview

StudyBible is a Python CLI application that generates comprehensive biblical exegesis for all 31,102 verses of the Protestant canon (66 books). Each verse includes:

- **Original Language Texts**: Hebrew (Westminster Leningrad Codex via OSHB) and Greek (SBLGNT)
- **Four Translations**: Original script, faithful direct translation, standalone English, amplified narrative
- **Exegetical Synthesis**: Ten comprehensive analysis dimensions including:
  - Literal-Primary Filter (Sensus Literalis)
  - Prophetic Typology & Intertextuality
  - Linguistic Mechanics & Names
  - Literary Devices
  - Numerical & Gematria Significance
  - Historical Context & Chronology
  - Socio-Political Matrix
  - Geospatial Data & Physical Geography
  - Archaeological Confirmation
  - Aggregate Perspective & Analogia Scriptura
- **Life Application**: Practical guidance for contemporary living

## Features

- **AI-Powered Analysis**: Uses Google Gemini 2.5 Pro for deep reasoning and exegetical synthesis
- **Original Source Texts**: Direct extraction from OSHB (Hebrew) and SBLGNT (Greek) repositories
- **JSON Flat-File Database**: Structured data storage at `/data/{OT|NT}/{BOOK}/{CH}/{VS}.json`
- **Static Website**: Eleventy-powered site with custom isArray filter for flexible data rendering
- **GitHub Pages Deployment**: Automatic deployment via GitHub Actions
- **Comprehensive Testing**: 190 tests with 81% coverage, pytest-based test suite

## Live Website

Visit the live StudyBible at: **https://davidlary.github.io/StudyBible/**

**Currently available**: Acts Chapter 10 (17 verses with complete exegesis)
*Note: Generation in progress - target is all 48 verses of Acts 10*

## Installation

### Prerequisites

- Python 3.12+
- Node.js 20+
- Google Gemini API key ([Get one here](https://console.cloud.google.com/apis/credentials))
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

   **IMPORTANT**: Never commit `.env` to git! It contains your API key.

4. **Download source texts:**
   ```bash
   python -m src.cli download-sources
   ```

   This downloads:
   - OSHB (Open Scriptures Hebrew Bible) to `sources/morphhb/`
   - SBLGNT (SBL Greek New Testament) to `sources/sblgnt/`

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

Output will be written to: `data/NT/Acts/10/01.json`

### Generate Entire Chapter

```bash
python -m src.cli generate-chapter Acts 10
```

**Note**: This can take 2-3 hours for a 48-verse chapter due to API rate limits.

### Build Website

```bash
npm run build
# Output in website/_site/ directory
```

Or for development with live reload:
```bash
npm run serve
```

### Build Search Index

```bash
npm run search
```

### Run Tests

```bash
pytest                          # Run all tests
pytest --cov=src               # With coverage report
pytest tests/unit/              # Unit tests only
pytest -n auto                  # Parallel execution (faster)
```

## Project Structure

```
StudyBible/
├── src/                        # Python source code (10 core modules)
│   ├── config.py              # Configuration & environment management
│   ├── bible_structure.py     # 66-book canon structure (31,102 verses)
│   ├── source_fetcher.py      # Download OSHB/SBLGNT repositories
│   ├── verse_extractor.py     # Extract Hebrew/Greek text + morphology
│   ├── schema_validator.py    # JSON schema validation (11 mandatory checks)
│   ├── gemini_client.py       # Gemini API client with retry logic
│   ├── exegesis_generator.py  # Orchestrate generation pipeline
│   ├── data_writer.py         # Atomic write JSON files
│   ├── batch_processor.py     # Process multiple verses with checkpoints
│   └── cli.py                 # Command-line interface
├── tests/                     # Test suite (190 tests, 81% coverage)
│   ├── unit/                  # Unit tests for each module
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test fixtures and sample data
├── data/                      # Generated verse JSON files
│   └── NT/Acts/10/            # Acts chapter 10 (17 verses so far)
├── sources/                   # Biblical source texts (not in git)
│   ├── morphhb/               # OSHB (Hebrew) - cloned via download-sources
│   └── sblgnt/                # SBLGNT (Greek) - cloned via download-sources
├── website/                   # Eleventy static site
│   ├── .eleventy.js           # Eleventy config with custom isArray filter
│   ├── _includes/             # Layout templates (Nunjucks)
│   │   └── layout.njk         # Main layout with embedded CSS
│   ├── _data/                 # Data files
│   │   └── acts10_verses.js   # Loads Acts 10 JSON data
│   ├── acts/                  # Acts chapter pages
│   │   └── chapter-10.njk     # Acts 10 template (handles arrays & strings)
│   └── index.njk              # Homepage
├── schemas/                   # JSON validation schemas
│   └── verse_schema.json      # 58-field verse schema
├── .github/workflows/         # GitHub Actions CI/CD
│   └── deploy.yml             # Automated deployment to GitHub Pages
├── StudyPrompt.md             # Comprehensive exegetical requirements
├── requirements.txt           # Python dependencies
├── package.json               # Node dependencies + build scripts
├── .env.example               # Template for environment variables
├── .gitignore                 # Excludes .env, .claude, sources/, node_modules/
└── README.md                  # This file
```

## Technology Stack

### Backend
- **Python 3.12**: Core application
- **Google Gemini 2.5 Pro**: AI-powered exegetical analysis with thinking mode
- **pytest**: Testing framework (190 tests, 81% coverage)
- **lxml**: XML parsing for OSHB Hebrew texts
- **jsonschema**: JSON validation with 11 mandatory field checks
- **click**: CLI framework for command-line interface
- **rich**: Beautiful terminal output with progress bars

### Frontend
- **Eleventy 3.1.2**: Static site generator
- **Nunjucks**: Templating engine with custom filters
- **Pagefind 1.4.0**: Client-side full-text search
- **Custom isArray filter**: Handles mixed array/string data types

### Sources
- **OSHB**: Open Scriptures Hebrew Bible (Westminster Leningrad Codex)
- **SBLGNT**: Society of Biblical Literature Greek New Testament

### Deployment
- **GitHub Pages**: Static hosting at davidlary.github.io/StudyBible
- **GitHub Actions**: Automated CI/CD pipeline on every push

## Development

### Running Tests

```bash
# All tests with coverage report
pytest --cov=src --cov-report=html

# Specific test file
pytest tests/unit/test_exegesis_generator.py -v

# Parallel execution (faster)
pytest -n auto

# Integration tests only
pytest tests/integration/ -v
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

### Debugging Template Issues

If the website displays incorrectly:

1. **Build locally**: `npm run build`
2. **Check generated HTML**: `website/_site/acts/chapter-10/index.html`
3. **Verify data loading**: Check console output for "Loaded N verses"
4. **Test isArray filter**: Ensure arrays render as `<ul>`, strings as `<p>`

## Architecture

### Generation Pipeline

1. **Extract Verse**: Read Hebrew/Greek text from source repositories
   - OSHB: Parse XML files with lxml
   - SBLGNT: Parse text files
2. **Build Prompt**: Combine StudyPrompt.md with verse reference and text
3. **Generate Exegesis**: Call Gemini 2.5 Pro API with comprehensive prompt
   - Uses thinking mode for deep reasoning
   - Retry logic with exponential backoff
4. **Validate JSON**: Check against 58-field schema with 11 mandatory validations
   - Thematic cognates, name etymologies, prophetic types
   - Numerical data, literary devices, historical dates
   - Socio-political context, geospatial coordinates
   - Physical geography, archaeological data
   - All Scripture cross-references
5. **Write File**: Atomic write to `/data/{testament}/{book}/{chapter}/{verse}.json`

### Website Build

1. **Data Loading**: `website/_data/acts10_verses.js` reads JSON files
2. **Template Rendering**: Nunjucks templates with verse data
   - Custom `isArray` filter handles mixed data types
   - Arrays → `<ul>` bullet lists
   - Strings → `<p>` paragraphs with line breaks
3. **Static Generation**: Eleventy builds HTML pages to `website/_site/`
4. **Search Indexing**: Pagefind indexes all content for client-side search
5. **Deployment**: GitHub Actions builds and deploys to GitHub Pages

### Template Data Type Handling

The project handles **inconsistent data types** across verses:
- **Verse 1**: Arrays (e.g., `["item1", "item2"]`)
- **Verse 2**: Strings (e.g., `"paragraph 1\nparagraph 2"`)

**Solution**: Custom `isArray` filter in `.eleventy.js`:
```javascript
eleventyConfig.addFilter("isArray", function(value) {
  return Array.isArray(value);
});
```

Template logic:
```nunjucks
{% if field | isArray %}
  <ul>{% for item in field %}<li>{{ item }}</li>{% endfor %}</ul>
{% else %}
  <p>{{ field | replace("\n", "<br>") | safe }}</p>
{% endif %}
```

## Security Best Practices

### API Key Management

**CRITICAL**: Never commit API keys to git!

1. **Environment Variables**: Store API key in `.env` (git-ignored)
2. **Template File**: `.env.example` contains only placeholders
3. **Validation**: Code checks API key format (must start with "AIzaSy")
4. **Git History**: Previous exposed keys have been removed

### Protected Files (in .gitignore)

- `.env` - Contains real API key
- `.env.local` - Local environment overrides
- `.claude/` - Claude Code settings with API keys
- `sources/` - Downloaded biblical texts (large files)
- `node_modules/` - Node dependencies
- `website/_site/` - Generated static site

### Verifying Security

```bash
# Check for exposed API keys
git log --all -S "AIzaSy" --source --

# Verify .gitignore is working
git status --ignored

# Check for tracked sensitive files
git ls-files | grep -E "\.env|\.claude"
```

## API Usage & Costs

### Cost Estimation (Gemini 2.5 Pro)

- **Per Verse**: ~10-15KB input + ~5-10KB output = ~$0.01-0.02 per verse
- **Acts 10** (48 verses): ~$0.50-1.00
- **Full Bible** (31,102 verses): ~$300-600

### Rate Limits

- **Free Tier**: ~15 requests/minute
- **Estimated Time**:
  - Acts 10: 2-3 hours (48 verses at 3-4 minutes/verse)
  - Full Bible: 7-10 days continuous processing (31,102 verses)

### Optimization

- Batch processing with checkpoint/resume capability
- Exponential backoff on rate limit errors
- Atomic writes prevent data corruption
- Progress tracking every 10 verses

## Troubleshooting

### Common Issues

1. **"Layout not found" error**:
   - Use correct build command: `npm run build`
   - Or: `npx @11ty/eleventy --input=website --output=website/_site --config=website/.eleventy.js`

2. **"[object Object]" on website**:
   - Fixed! Custom `isArray` filter handles mixed data types
   - Rebuild with: `npm run build`

3. **API rate limit errors**:
   - Wait 60 seconds between batches
   - Check rate limits in Google Cloud Console

4. **Source files not found**:
   - Run: `python -m src.cli download-sources`
   - Verify: `sources/morphhb/` and `sources/sblgnt/` exist

5. **GitHub Pages showing old version**:
   - CDN cache can take 5-10 minutes to update
   - Check deployment status: `gh run list --limit 5`

## Contributing

This is a personal research project. Contributions welcome via issues and pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and add tests
4. Ensure tests pass: `pytest --cov=src`
5. Commit changes: `git commit -m "Add amazing feature"`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Roadmap

- [x] Generate Acts 10 verses (17/48 complete)
- [ ] Complete Acts 10 (31 verses remaining)
- [ ] Add full-text search with Pagefind
- [ ] Generate entire Book of Acts (28 chapters)
- [ ] Add verse cross-reference navigation
- [ ] Implement parallel processing for faster generation
- [ ] Add PDF export for offline study
- [ ] Generate complete New Testament (27 books)
- [ ] Generate complete Old Testament (39 books)

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Acknowledgments

- **OSHB**: Open Scriptures Hebrew Bible project - faithful Hebrew source text
- **SBLGNT**: Society of Biblical Literature and Logos Bible Software - critical Greek text
- **Google**: Gemini 2.5 Pro API for AI-powered analysis with thinking mode
- **Eleventy**: Excellent static site generator with flexible templating
- **CPF**: Context-Preserving Framework v4.3.0 for development assistance

## Contact

David Lary - [GitHub](https://github.com/davidlary)

**Project Link**: [https://github.com/davidlary/StudyBible](https://github.com/davidlary/StudyBible)

**Live Website**: [https://davidlary.github.io/StudyBible/](https://davidlary.github.io/StudyBible/)

---

*"Your word is a lamp to my feet and a light to my path." - Psalm 119:105*

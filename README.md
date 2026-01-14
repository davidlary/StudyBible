# StudyBible

High-fidelity biblical exegesis with interlinear analysis, fact-checking, comprehensive tagging, and AI-powered deep reasoning.

## Overview

StudyBible is a Python CLI application that generates comprehensive biblical exegesis for all 31,102 verses of the Protestant canon (66 books). Each verse includes:

- **Interlinear Analysis**: Word-by-word morphology with Strong's numbers, parsing codes, transliteration (like Blue Letter Bible)
- **Original Language Texts**: Hebrew (Westminster Leningrad Codex via OSHB) and Greek (SBLGNT)
- **Four Translations**: Original script, faithful direct translation, standalone English, amplified narrative
- **Geographic Calculations**: Straight-line and ancient route distances, elevations, travel times
- **Comprehensive Tags**: 60+ categories across 5 tiers for database-like searching
- **Fact-Checking Pipeline**: Multi-tier validation using Grok API (xAI)
- **Exegetical Synthesis**: Ten comprehensive analysis dimensions including:
  - Linguistic Mechanics & Etymology
  - Textual & Contextual Analysis
  - Scripture Interpreting Scripture
  - Practical Application
  - Prophetic Typology & Intertextuality
  - Historical Context & Chronology
  - Geography & Physical Setting
  - Socio-Political Context
  - Archaeological Confirmation
  - Literary Devices

## Features

- **AI-Powered Analysis**: Google Gemini 2.5 Pro for deep reasoning + Grok API for fact-checking
- **True Interlinear**: Word-by-word Greek/Hebrew analysis with morphology and Strong's numbers
- **Geographic Intelligence**: Distance calculations, elevations, travel time estimates with uncertainty notes
- **Comprehensive Tagging**: 60+ tag categories (people, places, concepts, literary devices, etc.)
- **Multi-Tier Fact-Checking**: Ground truth → Database → AI review with auto-correction
- **Original Source Texts**: Direct extraction from OSHB (Hebrew) and SBLGNT (Greek) repositories
- **JSON Flat-File Database**: Structured data with tag indexes for static site searching
- **Static Website**: Eleventy-powered site with responsive design (70ch → 90ch)
- **GitHub Pages Deployment**: Automatic deployment via GitHub Actions
- **Comprehensive Testing**: 19+ unit tests for fact-checking pipeline

## Live Website

Visit the live StudyBible at: **https://davidlary.github.io/StudyBible/**

**Currently available**: Acts Chapter 10 (18 verses with complete interlinear analysis and fact-checking)

## Installation

### Prerequisites

- Python 3.12+
- Node.js 20+
- Google Gemini API key ([Get one here](https://console.cloud.google.com/apis/credentials))
- xAI Grok API key (optional, for fact-checking)
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

   API keys are configured via `~/Dropbox/Environments/.env-keys.yml`:
   ```yaml
   google_api_key: 'your-gemini-api-key-here'
   xai_api_key: 'your-grok-api-key-here'
   ```

   Then load them:
   ```bash
   source ~/Dropbox/Environments/Code/StudyBible/load_api_keys.sh
   ```

   **IMPORTANT**: API keys stored in environment variables only, never committed to git.

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
python -m src.cli generate Acts 10 1
```

Output written to: `data/NT/Acts/10/01.json`

### Generate Entire Chapter

```bash
python -m src.cli generate-chapter Acts 10
```

**Note**: This takes 2-4 hours for a 48-verse chapter due to API rate limits (~1 verse/minute).

### Build Tag Indexes

```bash
python3 src/tag_indexer.py
```

Generates search indexes in `website/_data/`:
- `tag_index.json` - Flat index for JavaScript filtering
- `tag_categories.json` - Category summaries
- `verse_tags.json` - Per-verse tag lists

### Build Website

```bash
npm run build
# Output in website/_site/ directory
```

Or for development with live reload:
```bash
npm run serve
```

### Run Tests

```bash
pytest tests/unit/test_fact_checker.py -v    # Fact-checking tests (19 tests)
pytest --cov=src                              # With coverage report
pytest -n auto                                # Parallel execution
```

## Project Structure

```
StudyBible/
├── src/                        # Python source code
│   ├── config.py              # API key handling (YAML parsing fix)
│   ├── bible_structure.py     # 66-book canon (31,102 verses)
│   ├── source_fetcher.py      # Download OSHB/SBLGNT
│   ├── verse_extractor.py     # Extract Hebrew/Greek + morphology
│   ├── schema_validator.py    # JSON schema validation
│   ├── gemini_client.py       # Gemini API client
│   ├── exegesis_generator.py  # Generation pipeline
│   ├── fact_checker.py        # Multi-tier fact-checking (NEW)
│   ├── tag_indexer.py         # Tag extraction & indexing (NEW)
│   ├── data_writer.py         # Atomic JSON writes
│   ├── batch_processor.py     # Batch with checkpoints
│   └── cli.py                 # Command-line interface
├── tests/                     # Test suite
│   ├── unit/test_fact_checker.py  # 19 tests for fact-checking
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test fixtures
├── data/                      # Generated verse JSON files
│   └── NT/Acts/10/            # Acts 10 (18 verses)
├── sources/                   # Biblical source texts (git-ignored)
│   ├── morphhb/               # OSHB (Hebrew)
│   └── sblgnt/                # SBLGNT (Greek)
├── website/                   # Eleventy static site
│   ├── .eleventy.js           # Custom filters (isArray, markdownItalics)
│   ├── _includes/             # Layout templates
│   ├── _data/                 # Data files + tag indexes
│   │   ├── tag_index.json         # Flat tag index (generated)
│   │   ├── tag_categories.json    # Tag summaries (generated)
│   │   └── verse_tags.json        # Per-verse tags (generated)
│   ├── acts/                  # Acts chapter pages
│   │   └── chapter-10.njk     # Acts 10 (updated for new schema)
│   └── index.njk              # Homepage
├── schemas/                   # JSON validation schemas
│   └── verse_schema.json      # 70+ field schema (updated)
├── vocabularies/              # Controlled vocabularies (NEW)
│   └── controlled_terms.json  # Consistent terminology
├── .github/workflows/         # GitHub Actions
│   └── deploy.yml             # Auto-deployment
├── StudyPrompt.md             # 300+ line comprehensive prompt
├── CLAUDE_README.md           # Context for Claude Code sessions (NEW)
├── IMPLEMENTATION_COMPLETE.md # Full implementation report (NEW)
├── USER_SUMMARY.md            # Quick-start guide (NEW)
├── requirements.txt           # Python dependencies
└── package.json               # Node dependencies
```

## Technology Stack

### Backend
- **Python 3.12**: Core application
- **Google Gemini 2.5 Pro**: Exegetical analysis with thinking mode
- **Grok API (xAI)**: Fact-checking and validation
- **pytest**: Testing framework (19+ tests)
- **lxml**: XML parsing for OSHB
- **jsonschema**: JSON validation
- **requests**: HTTP client for APIs

### Frontend
- **Eleventy 3.1.2**: Static site generator
- **Nunjucks**: Templating with custom filters
  - `isArray`: Handle mixed data types
  - `markdownItalics`: Convert *text* to <em>text</em>
- **Pagefind 1.4.0**: Client-side search (planned)
- **Responsive CSS**: 70ch → 90ch on wide screens

### Sources
- **OSHB**: Westminster Leningrad Codex (Hebrew/Aramaic)
- **SBLGNT**: SBL Greek New Testament

### Deployment
- **GitHub Pages**: Static hosting
- **GitHub Actions**: Automated CI/CD

## Architecture

### Generation Pipeline

1. **Extract Verse**: Read Hebrew/Greek from source repos
2. **Build Prompt**: Combine StudyPrompt.md (300+ lines) with verse data
3. **Generate Exegesis**: Call Gemini 2.5 Pro
4. **Fact-Check**: Multi-tier validation
   - TIER 1: Ground truth (verse refs, original text, cross-refs)
   - TIER 2: Database (coordinates, dates)
   - TIER 3: Expert AI review (Grok API)
   - Auto-correction loop (max 3 retries)
5. **Validate JSON**: Check against schema (70+ fields)
6. **Write File**: Atomic write to `data/{OT|NT}/{BOOK}/{CH}/{VS}.json`

### Fact-Checking Pipeline (NEW)

Multi-tier validation ensures accuracy:

1. **Ground Truth Checks**:
   - Verse reference validity
   - Original language text match (SBLGNT/OSHB)
   - Cross-reference verification

2. **Database Verification**:
   - Geographic coordinates (-90 to 90 lat, -180 to 180 long)
   - Historical dates (reasonable ranges)

3. **Expert AI Review**:
   - Grok API analyzes exegetical content
   - Checks historical accuracy, theological soundness
   - Auto-correction on failures (up to 3 attempts)

**Result**: `FactCheckResult` with issues, warnings, overall pass/fail

### Tag System (NEW)

Comprehensive tagging for database-like functionality:

**5-Tier Taxonomy** (60+ categories):
1. **Foundational Theology**: deity, trinity, salvation, sin
2. **Applied Theology**: prayer, worship, spiritual_disciplines
3. **Relational Ethics**: love, justice, humility
4. **Cultural Historical**: people, places, nationalities, professions
5. **Literary Prophetic**: literary_devices, prophecies, types_shadows

**Implementation**:
- Tags nested in verse JSON
- Flat indexes generated by `tag_indexer.py`
- JavaScript filtering (planned)

### Template Rendering Fixes

**Challenge**: Mixed data structures in JSON
- Some fields are strings
- Some are lists of strings
- Some are lists of dicts
- Some are dicts with nested fields

**Solution**: Custom Nunjucks logic
```nunjucks
{# Handle list of dicts #}
{% for item in linguistic_mechanics_and_names %}
  {% if item.entry %}
    <p><strong>{{item.entry}}:</strong> {{item.theological_significance}}</p>
  {% endif %}
{% endfor %}

{# Handle dicts with specific keys #}
{% if propheticData.type_shadow %}
  <p><strong>Type/Shadow:</strong> {{propheticData.type_shadow | markdownItalics | safe}}</p>
{% endif %}

{# Handle coordinates dict #}
<p>{{coordinates.lat}}°N, {{coordinates.long}}°E</p>
```

## API Key Configuration (IMPORTANT)

API keys are managed via YAML file:

**Location**: `/Users/davidlary/Dropbox/Environments/.env-keys.yml`

**Format**:
```yaml
google_api_key: 'AIzaSy...'
xai_api_key: 'xai-...'
```

**Loading**: `source load_api_keys.sh` (run before each session)

**Security**:
- Keys stored in environment variables only
- Never committed to git
- `src/config.py` handles malformed environment variables by reading YAML directly

## API Usage & Costs

### Cost Estimation

**Gemini 2.5 Pro**:
- Per Verse: ~$0.02-0.03 (with thinking mode)
- Acts 10 (48 verses): ~$1-1.50
- Full Bible (31,102 verses): ~$600-900

**Grok API** (fact-checking):
- Per Verse: ~$0.01-0.02
- Acts 10: ~$0.50-1.00

### Rate Limits

- **Gemini Free Tier**: ~15 requests/minute
- **Processing Speed**: ~1 verse/minute with thinking mode
- **Estimated Time**:
  - Acts 10: 2-4 hours (48 verses)
  - Full Bible: 7-14 days continuous

## Roadmap

- [x] Interlinear analysis (word-by-word morphology)
- [x] Fact-checking pipeline (Grok API)
- [x] Comprehensive tags (60+ categories)
- [x] Geographic calculations (distances, elevations)
- [x] Responsive design (70ch → 90ch)
- [x] Generate Acts 10:1-18 (18/48 complete)
- [ ] Complete Acts 10 (30 verses remaining)
- [ ] Tag search UI (JavaScript filtering)
- [ ] Full-text search (Pagefind integration)
- [ ] Generate entire Book of Acts (28 chapters)
- [ ] Complete New Testament (27 books)
- [ ] Complete Old Testament (39 books)

## Troubleshooting

### Common Issues

1. **API Key Not Working**:
   - Check YAML file: `~/Dropbox/Environments/.env-keys.yml`
   - Reload keys: `source load_api_keys.sh`
   - Test: `python3 -c "from src.config import get_gemini_api_key; print(get_gemini_api_key())"`

2. **[object Object] Rendering**:
   - Fixed via custom template logic for nested structures
   - Rebuild: `npm run build`

3. **Coordinates Not Showing**:
   - Fixed via dict rendering: `{{coordinates.lat}}°N, {{coordinates.long}}°E`

4. **Italics Not Rendering** (*text* showing as-is):
   - Fixed via `markdownItalics` filter
   - Converts `*word*` to `<em>word</em>`

5. **GitHub Pages Caching**:
   - Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
   - CDN takes 5-10 minutes to update

## Security Best Practices

**CRITICAL**: API keys managed via environment variables only

1. **YAML Configuration**: Keys in `~/Dropbox/Environments/.env-keys.yml`
2. **Git Exclusion**: YAML file not in repository
3. **Session Loading**: `source load_api_keys.sh` before each session
4. **Fallback**: `src/config.py` reads YAML directly if env var malformed

**Protected in .gitignore**:
- `.env-keys.yml`
- `load_api_keys.sh` (generated, may contain bugs)
- `.claude/` (Claude Code settings)
- `sources/` (large downloaded files)
- `node_modules/`

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- **OSHB**: Open Scriptures Hebrew Bible project
- **SBLGNT**: Society of Biblical Literature + Logos Bible Software
- **Google**: Gemini 2.5 Pro API
- **xAI**: Grok API for fact-checking
- **Eleventy**: Static site generator
- **CPF v4.3.0**: Development framework

## Contact

David Lary - [GitHub](https://github.com/davidlary)

**Project**: [https://github.com/davidlary/StudyBible](https://github.com/davidlary/StudyBible)

**Live Site**: [https://davidlary.github.io/StudyBible/](https://davidlary.github.io/StudyBible/)

---

*"Your word is a lamp to my feet and a light to my path." - Psalm 119:105*

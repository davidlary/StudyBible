# SICE v6.0 - Symphonic Intelligence Curation Engine

**Artist**: Trippen Aliens
**Author**: David Lary <davidlary@me.com>
**Version**: 6.0.0
**License**: MIT

---

## Overview

SICE (Symphonic Intelligence Curation Engine) is a production-ready Python pipeline that analyzes, scores, and curates music libraries using **dual-domain analysis**:

- **Domain A (Objective)**: Psychoacoustic measurements (roughness, sharpness, fluctuation, spectral entropy, inharmonicity, LUFS/True Peak)
- **Domain B (Subjective)**: Musicology features (phonetic openness, vibe classification, prosodic flux)

### Three Core Objectives

1. **Playlist Optimization**: Generate narrative-sequenced playlists following the Hero's Journey arc
2. **DistroKid Distribution**: SEO-optimized metadata, tags, and Hit Potential Scores
3. **Research Database**: Comprehensive metrics database (DuckDB) for catalog intelligence

---

## Features

- 🎵 **15+ Psychoacoustic Metrics**: Roughness (Vassilakis 2001), Sharpness (DIN 45692), Fluctuation Strength, Spectral Entropy, Inharmonicity
- 📊 **Hit Potential Score (HPS)**: Weighted composite score (0-100) with diagnostic explanations
- 🎭 **5 Vibe Clusters**: K-means classification (Driving-Aggressive, Ethereal-Ambient, Anthemic-Transcendent, Intimate-Reflective, Rhythmic-Groovy)
- 📖 **Hero's Journey Sequencing**: Narrative-driven playlist ordering (The Hook → The Climax → The Resolution)
- 🚀 **High Performance**: Multi-core parallel processing (8 workers), 2000+ tracks in <3 hours
- 💾 **Smart Caching**: SHA256-based cache with version invalidation, >80% hit rate on re-analysis
- 🎯 **DistroKid Ready**: SEO tags, mood/activity mappings, 200-char artist bios

---

## Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Psychoacoustics | mosqito | 1.2.1 |
| MIR Features | essentia | 2.1b6+ |
| Audio Analysis | librosa | 0.11.0 |
| Loudness | pyloudnorm | 0.1.1 |
| Database | DuckDB | 0.9+ |
| CLI | Click | 8.1+ |
| Testing | pytest | 7.4+ |

---

## Installation

### Prerequisites

- Python 3.9 - 3.12
- macOS, Linux, or Windows (with WSL2)
- 8 GB RAM minimum (16 GB recommended for 2000+ tracks)

### Quick Start

```bash
# Clone repository
git clone https://github.com/davidlary/PrepareForDistrokit.git
cd PrepareForDistrokit

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Configure environment
cp .env.template .env
# Edit .env with your library path

# Verify installation
sice --version
pytest tests/ --cov
```

---

## Usage

### Analyze Music Library

```bash
# Full library analysis (2000+ tracks, ~3 hours on 8 cores)
sice analyze /Users/davidlary/Dropbox/Music/MyMusic --workers 8

# Resume interrupted analysis
sice analyze /Users/davidlary/Dropbox/Music/MyMusic --resume

# Analyze single track
sice analyze-track /path/to/track.wav
```

### Generate Outputs

```bash
# Generate all outputs (Master Table, DistroKid JSON, Playlists)
sice generate --master-table --distrokit --playlists

# Master Intelligence Table only
sice generate --master-table

# Show statistics
sice stats
```

### Export Data

```bash
# Export to Parquet (fastest, smallest)
sice export --format parquet --output results.parquet

# Export to CSV (Excel-compatible)
sice export --format csv --output results.csv
```

---

## Output Files

After analysis, SICE generates:

1. **Master Intelligence Table** (`outputs/master_intelligence_table.md`, `.csv`)
   - All tracks ranked by Hit Potential Score
   - Physical + subjective diagnostics ("Why" / "Why Not")

2. **DistroKid Metadata** (`outputs/distrokit_metadata.json`)
   - SEO-optimized tags per track
   - Mood/activity/genre mappings
   - 200-char artist bios per vibe cluster

3. **Optimized Playlists** (`outputs/playlists.yaml`)
   - Hero's Journey sequenced playlists
   - Narrative roles (Hook, Build, Climax, Fall, Resolution)
   - Coherence scores

4. **DuckDB Database** (`data/sice.duckdb`)
   - 5 tables: tracks, domain_a_metrics, domain_b_metrics, hit_scores, playlists
   - Query with DuckDB CLI or pandas

---

## Architecture

```
sice/
├── core/               # Foundation (audio_loader, cache_manager, db_manager)
├── analyzers/          # Domain A & B analyzers
│   ├── domain_a/      # Roughness, sharpness, spectral, loudness
│   └── domain_b/      # Phonetic, vibe, prosody
├── intelligence/       # Hit scorer, vibe clusterer, narrative sequencer
└── outputs/           # Master table, DistroKid, playlist generators
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

---

## Testing

```bash
# Run all tests with coverage
pytest tests/ --cov=sice --cov-report=html

# Unit tests only
pytest tests/unit/

# Integration tests
pytest tests/integration/

# View coverage report
open htmlcov/index.html
```

---

## Development

### Code Quality

```bash
# Format code
black sice/ tests/

# Lint
ruff check sice/ tests/

# Type check
mypy sice/
```

### Framework Compliance

This project uses the [Context-Preserving Framework v4.7.2](https://github.com/davidlary/ContextPreservingFramework) for:
- Progress tracking across sessions
- Automatic checkpointing at 65% context
- >80% test coverage enforcement
- Git integration with hooks

---

## Performance

| Task | Single Track | 2000 Tracks (8 cores) |
|------|--------------|------------------------|
| Audio Loading | 1s | 4 min |
| Domain A Analysis | 15s | 62 min |
| Domain B Analysis | 10s | 42 min |
| Hit Scoring | 0.1s | 0.4 min |
| Clustering | - | 2 min |
| Output Generation | - | 5 min |
| **TOTAL** | **~30s** | **~2.9 hours** |

---

## Roadmap

- [ ] ML-based Hero's Journey (reinforcement learning)
- [ ] Real-time analysis API (FastAPI)
- [ ] Spotify API integration (auto-upload playlists)
- [ ] Web dashboard (React + Plotly)
- [ ] Multi-language lyrics support

---

## Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests (>80% coverage required)
4. Commit changes (`git commit -m "Add amazing feature"`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open Pull Request

---

## License

MIT License - see [LICENSE](LICENSE) file.

---

## Citation

If you use SICE in research, please cite:

```bibtex
@software{sice2025,
  author = {Lary, David},
  title = {SICE: Symphonic Intelligence Curation Engine},
  year = {2025},
  url = {https://github.com/davidlary/PrepareForDistrokit},
  version = {6.0.0}
}
```

---

## Contact

**David Lary**
Email: davidlary@me.com
GitHub: [@davidlary](https://github.com/davidlary)

**Artist**: Trippen Aliens
Music Library: /Users/davidlary/Dropbox/Music/MyMusic

---

**Built with the [Context-Preserving Framework v4.7.2](https://github.com/davidlary/ContextPreservingFramework)**

"""
Configuration management for SICE v6.0.

Provides dataclasses for system-wide configuration including:
- Artist metadata (Trippen Aliens)
- Audio processing parameters (48kHz target)
- Database paths
- Analysis thresholds
- Parallel processing settings
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

__all__ = ["Config", "AnalyzerConfig", "HitScorerWeights"]


@dataclass
class Config:
    """Main SICE configuration."""

    # Project Metadata
    artist_name: str = "Trippen Aliens"
    version: str = "6.0.0"

    # Paths
    library_path: Path = Path("/Users/davidlary/Dropbox/Music/MyMusic")
    cache_dir: Path = Path(".sice_cache")
    db_path: Path = Path("data/sice.duckdb")
    output_dir: Path = Path("outputs")

    # Audio Processing
    target_sample_rate: int = 48000  # Hz - Psychoacoustic accuracy
    audio_format: str = "wav"

    # Performance
    num_workers: int = 8  # ProcessPoolExecutor workers
    batch_size: int = 100  # Tracks per batch
    enable_cache: bool = True

    # Analysis Thresholds
    lufs_target: float = -14.0  # LUFS
    true_peak_max: float = -1.0  # dB
    min_duration: float = 10.0  # seconds

    # Output Flags
    generate_markdown: bool = True
    generate_csv: bool = True
    generate_distrokit_json: bool = True
    generate_playlists_yaml: bool = True

    def __post_init__(self) -> None:
        """Ensure all paths are Path objects."""
        self.library_path = Path(self.library_path)
        self.cache_dir = Path(self.cache_dir)
        self.db_path = Path(self.db_path)
        self.output_dir = Path(self.output_dir)

    def create_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class AnalyzerConfig:
    """Configuration for individual analyzers."""

    version: str = "1.0.0"
    sample_rate: int = 48000
    enable_caching: bool = True

    # Domain A: Psychoacoustic Parameters
    roughness_frame_size: int = 2048
    sharpness_method: str = "din"  # DIN 45692
    fluctuation_method: str = "mosqito"

    # Domain B: Musicology Parameters
    high_energy_threshold: float = 0.7  # 70th percentile
    min_segment_duration: float = 5.0  # seconds


@dataclass
class HitScorerWeights:
    """Weights for Hit Potential Score calculation.

    All weights sum to 1.0 for interpretability.
    Negative weights indicate inverse relationship (e.g., lower roughness = higher score).
    """

    # Domain A: Objective Psychoacoustics (60% weight total)
    roughness: float = -0.08  # Lower = better
    sharpness: float = -0.05  # Lower = better
    fluctuation: float = 0.07  # Moderate = engaging
    spectral_entropy: float = 0.10  # Higher = more complex/interesting
    inharmonicity: float = -0.06  # Lower = more tonal
    lufs_compliance: float = 0.15  # Critical for streaming platforms
    true_peak_compliance: float = 0.10  # Prevent clipping

    # Domain B: Subjective Musicology (40% weight total)
    phonetic_openness: float = 0.12  # High PO = catchy vocals
    energy_std: float = 0.08  # Dynamic range
    tempo_bpm: float = 0.06  # Optimal: 110-130 BPM
    pulse_clarity: float = 0.10  # Clear rhythm = danceable
    tonal_stability: float = 0.09  # Melodic coherence
    prosodic_flux: float = 0.06  # Lyrics-rhythm alignment

    def __post_init__(self) -> None:
        """Validate weights sum to approximately 1.0."""
        total = sum([
            abs(self.roughness),
            abs(self.sharpness),
            self.fluctuation,
            self.spectral_entropy,
            abs(self.inharmonicity),
            self.lufs_compliance,
            self.true_peak_compliance,
            self.phonetic_openness,
            self.energy_std,
            self.tempo_bpm,
            self.pulse_clarity,
            self.tonal_stability,
            self.prosodic_flux,
        ])
        if not (0.95 <= total <= 1.05):
            raise ValueError(f"Weights should sum to ~1.0, got {total:.3f}")

    def to_dict(self) -> dict[str, float]:
        """Return weights as dictionary."""
        return {
            "roughness": self.roughness,
            "sharpness": self.sharpness,
            "fluctuation": self.fluctuation,
            "spectral_entropy": self.spectral_entropy,
            "inharmonicity": self.inharmonicity,
            "lufs_compliance": self.lufs_compliance,
            "true_peak_compliance": self.true_peak_compliance,
            "phonetic_openness": self.phonetic_openness,
            "energy_std": self.energy_std,
            "tempo_bpm": self.tempo_bpm,
            "pulse_clarity": self.pulse_clarity,
            "tonal_stability": self.tonal_stability,
            "prosodic_flux": self.prosodic_flux,
        }

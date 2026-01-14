"""
CLI Module

Command-line interface for StudyBible generation.

Commands:
    generate: Generate exegesis for a single verse
    generate-chapter: Generate exegesis for entire chapter
    download-sources: Download biblical source texts
"""

import click
import sys
from pathlib import Path
from typing import Dict, Any

from src.config import (
    get_gemini_api_key,
    get_project_root,
    get_sources_directory
)
from src.batch_processor import process_verse, process_chapter
from src.source_fetcher import download_all_sources, get_oshb_path, get_sblgnt_path
from rich.console import Console
from rich.progress import Progress


# Rich console for formatted output
console = Console()


def load_config() -> Dict[str, Any]:
    """
    Load configuration for CLI commands.

    Returns:
        Configuration dictionary
    """
    base_path = get_project_root()
    sources_dir = get_sources_directory()

    config = {
        "base_path": base_path,
        "oshb_path": get_oshb_path(sources_dir),
        "sblgnt_path": get_sblgnt_path(sources_dir),
        "api_key": get_gemini_api_key(),
        "study_prompt_path": base_path / "StudyPrompt.md"
    }

    return config


@click.group()
def cli():
    """StudyBible - High-fidelity biblical exegesis generator."""
    pass


@cli.command()
@click.argument('book')
@click.argument('chapter', type=int)
@click.argument('verse', type=int)
def generate(book: str, chapter: int, verse: int):
    """Generate exegesis for a single verse.

    Example: studybible generate Genesis 1 1
    """
    try:
        console.print(f"[bold blue]Generating exegesis for {book} {chapter}:{verse}[/bold blue]")

        config = load_config()
        success = process_verse(book, chapter, verse, config)

        if success:
            console.print(f"[bold green]✓ Successfully generated {book} {chapter}:{verse}[/bold green]")
        else:
            console.print(f"[bold red]✗ Failed to generate {book} {chapter}:{verse}[/bold red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)


@cli.command()
@click.argument('book')
@click.argument('chapter', type=int)
@click.option('--start-verse', type=int, default=1, help='Verse to start from (for resuming)')
def generate_chapter(book: str, chapter: int, start_verse: int):
    """Generate exegesis for an entire chapter.

    Example: studybible generate-chapter Acts 10
    """
    try:
        console.print(f"[bold blue]Generating exegesis for {book} {chapter}[/bold blue]")

        config = load_config()
        results = process_chapter(book, chapter, config, start_verse=start_verse)

        # Display results
        console.print(f"\n[bold]Results:[/bold]")
        console.print(f"Total verses: {results['total']}")
        console.print(f"[green]Successful: {results['successful']}[/green]")
        if results['failed'] > 0:
            console.print(f"[red]Failed: {results['failed']}[/red]")

        if results['failed'] == 0:
            console.print(f"\n[bold green]✓ Chapter completed successfully![/bold green]")
        else:
            console.print(f"\n[bold yellow]⚠ Chapter completed with some failures[/bold yellow]")

    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)


@cli.command()
def download_sources():
    """Download biblical source texts (OSHB and SBLGNT).

    This command downloads the Hebrew and Greek source texts needed
    for verse extraction.
    """
    try:
        console.print("[bold blue]Downloading biblical sources...[/bold blue]")

        sources_dir = get_sources_directory()
        success = download_all_sources(sources_dir)

        if success:
            console.print("[bold green]✓ Sources downloaded successfully![/bold green]")
        else:
            console.print("[bold red]✗ Failed to download sources[/bold red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)


if __name__ == '__main__':
    cli()

"""
cursor-init: A CLI tool for initializing .cursorrules files.

This module contains the main CLI logic using Typer and Rich.
Supports both local templates and dynamic remote registry.
"""
from pathlib import Path
from typing import Optional

import typer
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from cursor_init.templates import TEMPLATES

# Initialize Typer app and Rich console
app = typer.Typer(
    name="cursor-init",
    help="🚀 Initialize your Cursor AI context in seconds.",
    add_completion=False,
)
console = Console()

# Constants
CURSORRULES_FILENAME = ".cursorrules"
REMOTE_REGISTRY_URL = "https://raw.githubusercontent.com/ThanhNguyxn/cursor-init/main/rules.json"
REQUEST_TIMEOUT = 5  # seconds


def fetch_remote_templates() -> dict:
    """
    Fetch templates from remote registry.
    
    Returns an empty dict if network fails (silent fallback).
    """
    try:
        response = requests.get(REMOTE_REGISTRY_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        # Validate structure
        if isinstance(data, dict) and "templates" in data:
            return data["templates"]
        return {}
    except (requests.RequestException, ValueError):
        # Silent fallback on any network or parsing error
        return {}


def get_all_templates() -> dict:
    """
    Get merged templates from local + remote sources.
    
    Remote templates override local ones if keys conflict.
    """
    # Start with local templates
    all_templates = TEMPLATES.copy()
    
    # Fetch and merge remote templates
    remote_templates = fetch_remote_templates()
    all_templates.update(remote_templates)
    
    return all_templates


def download_from_url(url: str) -> str:
    """
    Download content from a URL.
    
    Raises an exception if download fails.
    """
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def write_cursorrules(content: str, force: bool = False) -> Path:
    """
    Write content to .cursorrules file.
    
    Returns the path to the created file.
    Raises typer.Exit if user cancels overwrite.
    """
    cursorrules_path = Path.cwd() / CURSORRULES_FILENAME
    
    # Check if .cursorrules already exists
    if cursorrules_path.exists() and not force:
        console.print(
            f"\n[yellow]⚠️  Warning:[/yellow] A [bold]{CURSORRULES_FILENAME}[/bold] "
            "file already exists in this directory.\n"
        )
        overwrite = typer.confirm("Do you want to overwrite it?", default=False)
        if not overwrite:
            console.print("\n[dim]Operation cancelled.[/dim]\n")
            raise typer.Exit(code=0)
    
    # Write the content
    try:
        cursorrules_path.write_text(content, encoding="utf-8")
    except OSError as e:
        console.print(f"\n[red]❌ Error writing file:[/red] {e}\n")
        raise typer.Exit(code=1)
    
    return cursorrules_path


@app.command()
def list() -> None:
    """List all available cursor rule templates."""
    # Fetch all templates (local + remote)
    all_templates = get_all_templates()
    
    table = Table(
        title="📚 Available Cursor Rule Templates",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )

    table.add_column("Template", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Description", style="white")

    for key, template in sorted(all_templates.items()):
        table.add_row(key, template["name"], template["description"])

    console.print()
    console.print(table)
    console.print()
    console.print(
        "[dim]Usage: cursor-init install <template>[/dim]",
        justify="center",
    )
    console.print(
        "[dim]Or use: cursor-init install --url <link>[/dim]",
        justify="center",
    )
    console.print()


@app.command()
def install(
    name: Optional[str] = typer.Argument(
        None,
        help="The template name to install (e.g., python, nextjs, flutter)",
    ),
    url: Optional[str] = typer.Option(
        None,
        "--url", "-u",
        help="Install directly from a URL (e.g., --url https://example.com/rule.txt)",
    ),
    force: bool = typer.Option(
        False,
        "--force", "-f",
        help="Overwrite existing .cursorrules without asking",
    ),
) -> None:
    """
    Install a cursor rule template to the current directory.
    
    You can either:
    - Use a template name: cursor-init install python
    - Use a direct URL: cursor-init install --url https://example.com/rule.txt
    """
    # Validate: either name or url must be provided, but not both
    if url and name:
        console.print(
            "\n[red]❌ Error:[/red] Please use either a template name OR --url, not both.\n"
        )
        raise typer.Exit(code=1)
    
    if not url and not name:
        console.print(
            "\n[red]❌ Error:[/red] Please provide a template name or use --url.\n"
        )
        console.print("Examples:", style="yellow")
        console.print("  cursor-init install python", style="dim")
        console.print("  cursor-init install --url https://example.com/rule.txt", style="dim")
        console.print()
        raise typer.Exit(code=1)
    
    # Handle URL installation
    if url:
        console.print(f"\n[cyan]🌐 Downloading from:[/cyan] {url}\n")
        
        try:
            content = download_from_url(url)
        except requests.RequestException as e:
            console.print(f"\n[red]❌ Error downloading:[/red] {e}\n")
            raise typer.Exit(code=1)
        
        cursorrules_path = write_cursorrules(content, force)
        
        # Success message
        success_text = Text()
        success_text.append("✨ ", style="bold")
        success_text.append("Successfully installed cursor rules from URL!", style="green")
        
        console.print()
        console.print(Panel(success_text, border_style="green", padding=(0, 2)))
        console.print()
        console.print(f"[dim]Created:[/dim] [cyan]{cursorrules_path.absolute()}[/cyan]")
        console.print()
        return
    
    # Handle template name installation
    all_templates = get_all_templates()
    
    if name not in all_templates:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        console.print("Available templates:", style="yellow")
        for key in sorted(all_templates.keys()):
            console.print(f"  • {key}", style="dim")
        console.print()
        console.print("[dim]Tip: You can also use --url to install from any URL[/dim]")
        console.print()
        raise typer.Exit(code=1)

    template = all_templates[name]
    cursorrules_path = write_cursorrules(template["content"], force)

    # Success message
    success_text = Text()
    success_text.append("✨ ", style="bold")
    success_text.append("Successfully initialized cursor rules for ", style="green")
    success_text.append(template["name"], style="bold green")
    success_text.append("!", style="green")

    console.print()
    console.print(Panel(success_text, border_style="green", padding=(0, 2)))
    console.print()
    console.print(f"[dim]Created:[/dim] [cyan]{cursorrules_path.absolute()}[/cyan]")
    console.print()


@app.command()
def show(
    name: str = typer.Argument(
        ...,
        help="The template name to preview (e.g., python, nextjs, flutter, java-spring)",
    ),
) -> None:
    """Preview a cursor rule template without installing it."""
    all_templates = get_all_templates()
    
    if name not in all_templates:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        console.print("Available templates:", style="yellow")
        for key in sorted(all_templates.keys()):
            console.print(f"  • {key}", style="dim")
        console.print()
        raise typer.Exit(code=1)

    template = all_templates[name]

    console.print()
    console.print(
        Panel(
            template["content"],
            title=f"📄 {template['name']} Template",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()

"""
cursor-init: A CLI tool for initializing .cursorrules files.

This module contains the main CLI logic using Typer and Rich.
"""
from pathlib import Path

import typer
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


@app.command()
def list() -> None:
    """List all available cursor rule templates."""
    table = Table(
        title="📚 Available Cursor Rule Templates",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )

    table.add_column("Template", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Description", style="white")

    for key, template in TEMPLATES.items():
        table.add_row(key, template["name"], template["description"])

    console.print()
    console.print(table)
    console.print()
    console.print(
        "[dim]Usage: cursor-init install <template>[/dim]",
        justify="center",
    )
    console.print()


@app.command()
def install(
    name: str = typer.Argument(
        ...,
        help="The template name to install (e.g., python, nextjs, flutter, java-spring)",
    ),
) -> None:
    """Install a cursor rule template to the current directory."""
    # Check if template exists
    if name not in TEMPLATES:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        console.print("Available templates:", style="yellow")
        for key in TEMPLATES:
            console.print(f"  • {key}", style="dim")
        console.print()
        raise typer.Exit(code=1)

    template = TEMPLATES[name]
    cursorrules_path = Path.cwd() / CURSORRULES_FILENAME

    # Check if .cursorrules already exists
    if cursorrules_path.exists():
        console.print(
            f"\n[yellow]⚠️  Warning:[/yellow] A [bold]{CURSORRULES_FILENAME}[/bold] "
            "file already exists in this directory.\n"
        )
        overwrite = typer.confirm("Do you want to overwrite it?", default=False)
        if not overwrite:
            console.print("\n[dim]Operation cancelled.[/dim]\n")
            raise typer.Exit(code=0)

    # Write the template content to .cursorrules
    try:
        cursorrules_path.write_text(template["content"], encoding="utf-8")
    except OSError as e:
        console.print(f"\n[red]❌ Error writing file:[/red] {e}\n")
        raise typer.Exit(code=1)

    # Success message
    success_text = Text()
    success_text.append("✨ ", style="bold")
    success_text.append("Successfully initialized cursor rules for ", style="green")
    success_text.append(template["name"], style="bold green")
    success_text.append("!", style="green")

    console.print()
    console.print(Panel(success_text, border_style="green", padding=(0, 2)))
    console.print()
    console.print(
        f"[dim]Created:[/dim] [cyan]{cursorrules_path.absolute()}[/cyan]"
    )
    console.print()


@app.command()
def show(
    name: str = typer.Argument(
        ...,
        help="The template name to preview (e.g., python, nextjs, flutter, java-spring)",
    ),
) -> None:
    """Preview a cursor rule template without installing it."""
    # Check if template exists
    if name not in TEMPLATES:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        raise typer.Exit(code=1)

    template = TEMPLATES[name]

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

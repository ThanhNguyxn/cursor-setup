"""
cursor-init: Initialize your Cursor AI context in seconds.

A CLI tool that automates the creation of .cursorrules files.
"""

__version__ = "0.1.0"
__author__ = "cursor-init contributors"

from cursor_init.main import app, main
from cursor_init.templates import TEMPLATES

__all__ = ["app", "main", "TEMPLATES", "__version__"]

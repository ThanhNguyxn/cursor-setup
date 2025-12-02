# cursor-init 🚀

> **Stop copy-pasting. Initialize your Cursor AI context in seconds.**

[![PyPI version](https://badge.fury.io/py/cursor-init.svg)](https://badge.fury.io/py/cursor-init)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`cursor-init` is a CLI tool that automates the creation of `.cursorrules` files. Instead of manually searching the internet for AI coding instructions and copy-pasting them into your projects, simply run one command to get expert-level, production-ready cursor rules for your specific tech stack.

---

## ✨ Features

- 🎯 **One Command Setup** — Initialize cursor rules in seconds, not minutes
- 📚 **Curated Templates** — Expert-level rules for Python, Next.js, Flutter, Java Spring Boot, and more
- 🎨 **Beautiful CLI** — Powered by Rich for a delightful terminal experience
- 🔄 **Safe Overwrites** — Prompts for confirmation before replacing existing rules
- 🚀 **Zero Config** — Works out of the box with sensible defaults
- 📦 **Lightweight** — Minimal dependencies, fast installation

---

## 📦 Installation

```bash
pip install cursor-init
```

Or with [pipx](https://pipx.pypa.io/) for isolated installation:

```bash
pipx install cursor-init
```

---

## 🚀 Quick Start

### List Available Templates

See all available cursor rule templates:

```bash
cursor-init list
```

**Output:**

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Template    ┃ Name               ┃ Description                                         ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ python      │ Python             │ Modern Python with type hints, docstrings, and...  │
│ nextjs      │ Next.js            │ Next.js 14+ with App Router, Server Components...  │
│ flutter     │ Flutter            │ Flutter/Dart with clean architecture and best...   │
│ java-spring │ Java Spring Boot   │ Spring Boot 3+ with modern Java practices          │
└─────────────┴────────────────────┴─────────────────────────────────────────────────────┘
```

### Install a Template

Initialize cursor rules for your project:

```bash
cursor-init install python
```

**Output:**

```
╭──────────────────────────────────────────────────────────╮
│ ✨ Successfully initialized cursor rules for Python!     │
╰──────────────────────────────────────────────────────────╯

Created: /path/to/your/project/.cursorrules
```

### Preview a Template

Want to see what's in a template before installing?

```bash
cursor-init show python
```

---

## 📋 Available Templates

| Template | Description |
|----------|-------------|
| `python` | Modern Python with type hints, docstrings, PEP 8, pytest, and best practices |
| `nextjs` | Next.js 14+ with App Router, Server Components, Server Actions, and Tailwind CSS |
| `flutter` | Flutter/Dart with clean architecture, Riverpod, and widget best practices |
| `java-spring` | Spring Boot 3+ with modern Java 17+ features, JPA, and REST API patterns |

---

## 🤔 Why cursor-init?

### Before cursor-init 😫

1. Google "cursorrules for Python"
2. Find a random GitHub gist
3. Hope it's up-to-date and high quality
4. Manually copy-paste into your project
5. Repeat for every new project...

### After cursor-init 🎉

```bash
cursor-init install python
```

**Done.** Expert-level cursor rules, one command, every time.

---

## 🛠️ Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/ThanhNguyxn/cursor-init.git
cd cursor-init

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run the CLI
cursor-init --help
```

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black src/

# Lint
ruff src/

# Type check
mypy src/
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Adding a New Template

1. Fork the repository
2. Edit `src/cursor_init/templates.py`
3. Add your template to the `TEMPLATES` dictionary:

```python
"your-stack": {
    "name": "Your Stack",
    "description": "Brief description of the stack",
    "content": """# Your Stack Rules
    
Your expert-level cursor rules here...
"""
},
```

4. Submit a Pull Request

### Template Guidelines

- ✅ Include actual, actionable rules (not placeholders)
- ✅ Cover coding style, best practices, and common patterns
- ✅ Keep templates focused and relevant
- ✅ Use clear, professional language

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Inspired by the amazing [Cursor](https://cursor.sh/) editor
- Built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)

---

<p align="center">
  Made with ❤️ for the developer community
</p>

<p align="center">
  <a href="https://github.com/ThanhNguyxn/cursor-init">⭐ Star us on GitHub</a>
</p>

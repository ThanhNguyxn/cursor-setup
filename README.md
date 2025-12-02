# cursor-init 🚀

> **Stop copy-pasting. Initialize your Cursor AI context in seconds.**

[![PyPI version](https://badge.fury.io/py/cursor-init.svg)](https://badge.fury.io/py/cursor-init)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**What is this?** A simple command-line tool that creates `.cursorrules` files for you. These files tell [Cursor AI](https://cursor.sh/) how to write better code for your specific project.

**No more:** Googling for rules → Finding outdated gists → Copy-pasting → Hoping it works

**Just run:** `cursor-init install python` ✨

---

## ✨ Features

- 🎯 **One Command Setup** — Get started in seconds, not minutes
- 📚 **Curated Templates** — Expert-level rules for Python, Next.js, Flutter, Java Spring Boot, and more
- 🌐 **Dynamic Updates** — Automatically fetches the latest templates from the cloud
- 🔗 **Install from URL** — Use any cursorrules file from the internet
- 🎨 **Beautiful CLI** — Colorful, easy-to-read terminal output
- 🔄 **Safe Overwrites** — Always asks before replacing existing files

---

## 📦 Installation

Open your terminal and run:

```bash
pip install cursor-init
```

That's it! You can now use `cursor-init` anywhere on your computer.

> 💡 **Tip:** If you get a permission error, try `pip install --user cursor-init`

---

## 🚀 Quick Start

**The fastest way to get started:**

```bash
# Go to your project folder
cd your-project

# Install Python rules (or replace "python" with your stack)
cursor-init install python
```

Done! Check your folder — you now have a `.cursorrules` file. 🎉

---

## 📖 How to Use

### 1️⃣ See What's Available

First, let's see all the templates you can use:

```bash
cursor-init list
```

This shows you a nice table with all available templates:

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Template    ┃ Name               ┃ Description                            ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ python      │ Python             │ Modern Python with type hints...       │
│ nextjs      │ Next.js            │ Next.js 14+ with App Router...         │
│ flutter     │ Flutter            │ Flutter/Dart with clean architecture...│
│ java-spring │ Java Spring Boot   │ Spring Boot 3+ with modern Java...     │
│ golang      │ Go                 │ Go with best practices...              │
└─────────────┴────────────────────┴────────────────────────────────────────┘
```

### 2️⃣ Install a Template

Pick a template and install it:

```bash
# For a Python project
cursor-init install python

# For a Next.js project
cursor-init install nextjs

# For a Flutter app
cursor-init install flutter
```

You'll see a success message:

```
╭──────────────────────────────────────────────────────────╮
│ ✨ Successfully initialized cursor rules for Python!     │
╰──────────────────────────────────────────────────────────╯

Created: /home/you/your-project/.cursorrules
```

### 3️⃣ Preview Before Installing

Want to see what's inside a template first?

```bash
cursor-init show python
```

This prints the full content so you can review it.

---

## 🔧 Advanced Usage

### Install from Any URL

Got a cursorrules file from a friend or found one online? Install it directly:

```bash
# Install from any URL
cursor-init install --url https://example.com/my-custom-rules.txt
```

**Real example** — Install from the awesome-cursorrules repo:

```bash
cursor-init install --url https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/golang.cursorrules
```

### Force Overwrite

Already have a `.cursorrules` file? Use `--force` to skip the confirmation:

```bash
cursor-init install python --force
```

### Short Flags

Use `-u` for URL and `-f` for force:

```bash
cursor-init install -u https://example.com/rules.txt -f
```

---

## 📋 Available Templates

| Template | Best For |
|----------|----------|
| `python` | Python projects with type hints, docstrings, pytest |
| `nextjs` | Next.js 14+ with App Router, Server Components, Tailwind |
| `flutter` | Flutter/Dart mobile apps with clean architecture |
| `java-spring` | Spring Boot 3+ REST APIs with modern Java |
| `golang` | Go projects with idiomatic patterns |

> 💡 Run `cursor-init list` to see the latest templates (we add more regularly!)

---

## 🤔 Why cursor-init?

### Before 😫

1. Google "cursorrules for Python"
2. Find a random GitHub gist from 2023
3. Hope it's still accurate
4. Copy-paste into your project
5. Repeat for every single project...

### After 🎉

```bash
cursor-init install python
```

**One command. Expert rules. Every time.**

---

## 🛠️ Development

Want to contribute or run locally?

```bash
# Clone the repo
git clone https://github.com/ThanhNguyxn/cursor-init.git
cd cursor-init

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in dev mode
pip install -e ".[dev]"

# Test it works
cursor-init --help
```

---

## 🤝 Contributing

We'd love your help! Here's how:

### Add a New Template

1. Fork this repository
2. Edit `src/cursor_init/templates.py`
3. Add your template:

```python
"your-stack": {
    "name": "Your Stack",
    "description": "Brief description",
    "content": """# Your rules here...
"""
},
```

4. Submit a Pull Request!

### Template Guidelines

- ✅ Include real, actionable rules (not placeholders)
- ✅ Cover coding style, best practices, common patterns
- ✅ Keep it focused and relevant
- ✅ Use clear, professional language

---

## 📄 License

MIT License — use it however you want!

---

## 🙏 Acknowledgments

- Inspired by the amazing [Cursor](https://cursor.sh/) editor
- Built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)
- Thanks to all contributors! ❤️

---

<p align="center">
  <b>Found this useful?</b>
</p>

<p align="center">
  <a href="https://github.com/ThanhNguyxn/cursor-init">⭐ Give us a star on GitHub!</a>
</p>

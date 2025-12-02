# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-12-02

### Added

- Initial release of cursor-init CLI tool
- `cursor-init list` command to display available templates
- `cursor-init install <template>` command to install cursor rules
- `cursor-init show <template>` command to preview templates
- `--url` flag to install from any URL directly
- `--force` flag to skip overwrite confirmation
- Dynamic template registry from remote `rules.json`
- Silent fallback to local templates when network fails
- Built-in templates for:
  - Python (type hints, docstrings, PEP 8)
  - Next.js (App Router, Server Components, Tailwind)
  - Flutter (clean architecture, Riverpod)
  - Java Spring Boot (Spring Boot 3+, modern Java)
- Remote templates for:
  - Go/Golang
  - Rust
  - TypeScript
  - React
  - Vue.js

### Technical

- Built with Typer for CLI framework
- Rich for beautiful terminal output
- Requests for HTTP fetching
- Supports Python 3.9+

[Unreleased]: https://github.com/ThanhNguyxn/cursor-init/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ThanhNguyxn/cursor-init/releases/tag/v0.1.0

# Changelog

All notable changes to this project will be documented in this file.

The project follows **Semantic Versioning** and uses the **Keep a Changelog** format.

---

## [Unreleased]

### Documentation

- Updated README to reflect the current project architecture.
- Improved project documentation.
- Updated roadmap and project structure.

---

## [0.2.0] - 2026-08-03

### Added

- External system prompt (`system_prompt.md`)
- Prompt loader module
- Centralized application settings module (`settings.py`)
- Dedicated `prompts` directory
- Dedicated `config` directory
- Professional documentation workflow
- Custom logging system
- Logger class with centralized logging
- Automatic log directory creation
- Timestamped log entries

### Changed

- Moved the system prompt out of the source code into an external Markdown file.
- Replaced hardcoded prompt loading with `prompt_loader.py`.
- Moved AI model configuration into the centralized settings module.
- Improved project architecture by separating prompts and configuration.
- Replaced relative prompt paths with `pathlib` for reliable file loading.
- Improved overall project maintainability.
- Replaced console print statements with the custom logger
- Improved the configuration package structure
- Added module documentation for configuration modules

### Fixed

- Fixed prompt loading when starting the application from different working directories.

---

## [0.1.0] - 2026-07-28

### Added

- Initial project structure
- OpenAI API integration
- Runtime conversation memory
- AI core module
- Chat module
- Startup module
- Modular architecture
- Git version control
- GitHub repository
- Initial README
- Initial ROADMAP
- Initial CHANGELOG
- Custom system prompt

### Security

- Added `.gitignore`
- Excluded `.env` from version control
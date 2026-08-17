# Changelog

All notable changes to this project will be documented in this file.

The project follows **Semantic Versioning** and uses the **Keep a Changelog** format.

---

## [Unreleased]

No changes yet.

---

## [0.3.0] - 2026-08-17

### Added

- SQLite database foundation
- Database connection management
- Database schema initialization
- Conversation model
- Message model
- Conversation repository
- Message repository
- Conversation CRUD operations
- Message CRUD operations
- Conversation service
- Message service
- Persistent conversation history
- Conversation selection
- AI conversation context restoration
- Conversation history loading after application restart
- Message creation and update support
- `created_at` and `updated_at` timestamps for conversations and messages
- Database `.db` files excluded from version control
- Chat integration with the database and service layers

### Changed

- Integrated the chat module with the conversation and message services.
- Replaced temporary runtime-only conversation context with persistent database-backed conversation history.
- Added loading of stored messages into the AI conversation context.
- Updated the chat flow to allow selecting existing conversations.
- Separated database access through repository and service layers.
- Improved application architecture by introducing a clear Database → Repository → Service → Chat flow.
- Updated the `.gitignore` configuration for SQLite databases.

### Fixed

- Fixed message timestamp handling by using `updated_at` when updating existing messages.
- Fixed conversation history restoration after restarting the application.
- Fixed message and conversation persistence across application sessions.
- Fixed conversation selection and message loading for existing conversations.

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
- Replaced console print statements with the custom logger.
- Improved the configuration package structure.
- Added module documentation for configuration modules.

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
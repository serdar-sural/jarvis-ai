# Jarvis AI

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.3.0-brightgreen)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular-blueviolet)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A modular AI assistant built with Python and OpenAI, focusing on clean architecture, maintainability, persistence, and professional software engineering practices.

Jarvis AI is a long-term software engineering and AI engineering learning project. Rather than only building an intelligent assistant, the project focuses on understanding how professional software is designed, structured, tested, documented, and continuously improved.

---

# Project Goals

The primary goals of this project are:

- Learn Artificial Intelligence Engineering
- Learn Professional Software Engineering
- Build a scalable AI assistant
- Practice Clean Architecture
- Apply professional Git workflows
- Follow modern development practices
- Continuously improve code quality
- Learn by understanding, not by copying

---

# Project Status

| Property | Value |
|-----------|-------|
| Version | **0.3.0** |
| Status | **Active Development** |
| Language | **Python** |
| Architecture | **Modular** |
| AI Provider | **OpenAI** |
| Database | **SQLite** |
| License | **MIT (planned)** |

---

# Features

Current features include:

- Modular project architecture
- OpenAI Chat Completions integration
- Runtime conversation memory
- Persistent conversation history
- Conversation selection
- AI conversation context restoration
- Conversation history restoration after application restart
- SQLite database integration
- Conversation and message persistence
- Conversation CRUD operations
- Message CRUD operations
- Conversation service
- Message service
- Repository layer
- External system prompt
- Prompt loader
- Centralized settings module
- Modular AI core
- Custom logging system
- Modular chat system
- Startup module
- Professional project structure
- Git version control
- Feature branch workflow
- Clean and maintainable codebase
- Automatic log directory creation
- Timestamped log entries

---

# Project Structure

```text
Jarvis_AI/
│
├── assets/
│
├── chat/
│   ├── __init__.py
│   └── chat.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── core/
│   ├── __init__.py
│   ├── ai.py
│   ├── logger.py
│   └── prompt_loader.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   ├── repository.py
│   └── models/
│       ├── __init__.py
│       ├── conversation.py
│       └── message.py
│
├── data/
│
├── logs/
│   └── .gitkeep
│
├── prompts/
│   └── system_prompt.md
│
├── services/
│   ├── __init__.py
│   ├── conversation_service.py
│   └── message_service.py
│
├── ui/
│   ├── __init__.py
│   └── startup.py
│
├── .gitignore
├── CHANGELOG.md
├── README.md
├── ROADMAP.md
├── main.py
└── requirements.txt
```

## Directory Overview

| Folder | Description |
|---------|-------------|
| **assets** | Images, icons and future project resources |
| **chat** | Handles the chat loop, conversation selection, and user interaction |
| **config** | Global application settings |
| **core** | Core AI logic, OpenAI communication, logging, and prompt loading |
| **database** | Database connection, repositories, and data models |
| **data** | Local application data and SQLite database storage |
| **logs** | Application log files generated during runtime |
| **prompts** | External AI prompt files |
| **services** | Application services that coordinate business logic |
| **ui** | Startup process and future user interface |
| **main.py** | Application entry point |

---

# Architecture

Jarvis AI follows the principle of **Separation of Concerns**.

The current architecture is organized into several layers:

```text
UI
 ↓
Chat
 ↓
Services
 ↓
Repositories
 ↓
Database
```

The AI layer works alongside the application flow:

```text
Chat
 ↓
AI Core
 ↓
OpenAI API
```

Each module has a specific responsibility:

- **chat** handles user interaction and conversation flow.
- **core** contains AI logic, OpenAI communication, logging, and prompt loading.
- **config** stores application settings.
- **prompts** contains external AI prompts.
- **services** contains application and business logic.
- **database** handles persistence through repositories and models.
- **ui** manages the startup process and user interface.
- **data** contains local application data and database storage.

This modular architecture keeps the project maintainable, scalable, and easy to extend.

---

# Technologies

Current technologies:

- Python
- OpenAI API
- SQLite
- python-dotenv
- Git
- GitHub

Additional technologies will be introduced as the project evolves.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/serdar-sural/jarvis-ai.git
```

Open the project directory:

```bash
cd jarvis-ai
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
python main.py
```

---

# Usage

After starting the application, Jarvis initializes the OpenAI client, loads the external system prompt, applies the application settings, and starts the interactive application.

Users can select an existing conversation and continue the conversation from its stored history.

Conversation messages are stored persistently in the local SQLite database and loaded back into the AI context when a conversation is selected.

This allows Jarvis to retain conversation context even after the application has been restarted.

---

# Development Workflow

Jarvis AI is developed using a professional Git workflow.

Every change follows the same process:

- Create a dedicated branch
- Implement the feature or fix
- Test the application
- Review the code
- Update documentation when necessary
- Create a Pull Request
- Merge into `main`
- Delete merged branches

This workflow keeps the project clean, maintainable, and easy to follow.

---

# Roadmap

Upcoming major milestones include:

- Long-term AI memory
- Advanced conversation management
- Improved error handling
- Multiple AI model support
- Tool integration
- Web search capabilities
- External API integration
- User authentication
- Desktop application
- Web application
- Voice interaction
- Automated testing
- Docker support
- Continuous Integration (CI)

For the complete development plan, see **ROADMAP.md**.

---

# Contributing

Contributions, ideas, suggestions, and constructive feedback are welcome.

Contribution guidelines will be added as the project evolves.

---

# License

This project is planned to be released under the MIT License.

A dedicated `LICENSE` file will be added in a future release.

---

# Author

**Serdar Süral**

Developed as a long-term AI Engineering and Software Engineering learning project.

---

⭐ If you find this project interesting, consider giving it a star on GitHub.
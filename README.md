# Jarvis AI

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.2.0-brightgreen)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular-blueviolet)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A modular AI assistant built with Python and OpenAI, focusing on clean architecture, maintainability, and professional software engineering practices.

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
| Version | **0.2.0** |
| Status | **Active Development** |
| Language | **Python** |
| Architecture | **Modular** |
| AI Provider | **OpenAI** |
| License | **MIT (planned)** |

---

# Features

Current features include:

- Modular project architecture
- OpenAI Chat Completions integration
- Runtime conversation memory
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
- Centralized logging system
- Automatic log directory creation
- Timestamped log entries

---

# Project Structure

```text
Jarvis_AI/
│
├── assets/
├── chat/
│   └── chat.py
├── config/
│   └── settings.py
├── core/
│   ├── ai.py
|   └── prompt_loader.py
├── data/
├── logs/
│   └── .gitkeep
├── prompts/
│   └── system_prompt.md
├── ui/
│   └── startup.py
├── .gitignore
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
└── main.py
```

## Directory Overview

| Folder | Description |
|---------|-------------|
| **assets** | Images, icons and future project resources |
| **chat** | Handles the chat loop and user interaction |
| **config** | Global application settings |
| **core** | Core AI logic and OpenAI communication |
| **data** | Future application data and storage |
| **prompts** | External AI prompt files |
| **ui** | Startup process and future user interface |
| **main.py** | Application entry point |
| **logs** | Application log files generated during runtime |

---

# Architecture

Jarvis AI follows the principle of **Separation of Concerns**.

Each module has a single responsibility:

- **chat** handles user interaction.
- **core** contains AI logic.
- **config** stores application settings.
- **prompts** contains external AI prompts.
- **ui** manages the user interface.
- **data** is reserved for persistent storage.

This modular architecture keeps the project maintainable, scalable, and easy to extend.

---

# Technologies

Current technologies:

- Python
- OpenAI API
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

After starting the application, Jarvis initializes the OpenAI client, loads the external system prompt, applies the application settings, and starts an interactive chat session.

Conversation history is stored during runtime and continuously provided to the AI model.

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

- Persistent conversation history
- Long-term AI memory
- Database integration
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
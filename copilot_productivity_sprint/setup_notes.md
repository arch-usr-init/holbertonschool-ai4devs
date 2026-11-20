# Setup Notes: Copilot Productivity Sprint

## 1. Development Environments (IDEs)
- **Primary IDE:** Visual Studio Code (VS Code)
  - Version: 1.98.2
- **Secondary Environment:** Antigravity
  - Version: 0.1.0

## 2. AI Coding Assistants
For this sprint, I am testing CLI-based AI assistants rather than IDE-integrated ones like GitHub Copilot. 
- **AI Assistant 1:** Codex CLI
  - Version: 0.1.0
  - Usage: Used for terminal-based prompt generation, boilerplate code creation, and script generation.
- **AI Assistant 2:** Claude Code CLI
  - Version: 0.2.9
  - Usage: Used for larger refactoring tasks, explaining complex code blocks, and generating unit tests directly via the terminal.

## 3. VS Code Extensions & Tooling
To track productivity metrics (time and code changes) during the sprint, the following extensions/tools are installed:
- **Time Tracking:** WakaTime
- **Version Control:** Git / GitHub Pull Requests and Issues
- **Testing/Linting:** Python, Pytest, and ESLint

## 4. Setup Process
1. Installed and authenticated VS Code and the Antigravity environment.
2. Installed and configured Codex CLI globally via terminal.
3. Installed and authenticated Claude Code CLI globally via terminal.
4. Disabled any other conflicting AI tab-completion tools (like Tabnine) to ensure a clean baseline for the "without AI" sprint.
5. Configured time-tracking mechanisms to manually record start/stop times for the benchmark tasks.

## 5. Benchmark Task Environment
- **Language:** Python 3.12 and Node.js 20
- **Package Manager:** pip and npm
- **Testing Framework:** pytest and Jest

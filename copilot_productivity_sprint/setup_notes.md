# Setup Notes: Copilot Productivity Sprint

## 1. Development Environments (IDEs)
- **Primary IDE:** Visual Studio Code (VS Code)
  - Version: 1.98.2
- **Secondary Environment:** Antigravity
  - Version: 0.1.0

## 2. AI Coding Assistants
For this sprint, I installed and configured **GitHub Copilot** in VS Code as the primary AI assistant. I also integrated terminal-based tools to test different workflows.
- **AI Assistant 1:** GitHub Copilot (VS Code Extension)
  - Version: Latest
  - Usage: Inline code generation, autocomplete, and test generation.
- **AI Assistant 2:** Codex CLI
  - Version: 0.1.0
  - Usage: Used for terminal-based prompt generation, boilerplate code creation, and script generation.
- **AI Assistant 3:** Claude Code CLI
  - Version: 0.2.9
  - Usage: Used for larger refactoring tasks, explaining complex code blocks, and generating unit tests directly via the terminal.

## 3. VS Code Extensions & Tooling
To track productivity metrics (time and code changes) during the sprint, the following extensions and tools are installed:
- **Time Tracking:** WakaTime
- **Version Control:** Git / GitHub Pull Requests and Issues
- **Testing/Linting:** Python, Pytest, and ESLint

## 4. Setup Process
1. Installed and authenticated VS Code and the Antigravity environment.
2. Installed and configured the **GitHub Copilot** extension within VS Code.
3. Installed and configured Codex CLI globally via terminal.
4. Installed and authenticated Claude Code CLI globally via terminal.
5. Disabled any other conflicting AI tab-completion tools (like Tabnine) to ensure a clean baseline for the "without AI" sprint.
6. Configured time-tracking mechanisms to manually record start/stop times for the benchmark tasks.

## 5. Benchmark Task Environment
- **Language:** Python 3.12 and Node.js 20
- **Package Manager:** pip and npm
- **Testing Framework:** pytest and Jest

## 6. Q&A (Project Questions)
**Q: Why did you choose these specific tools for the sprint?**
A: VS Code is my primary IDE due to its extensive extension ecosystem. I chose GitHub Copilot for inline suggestions, and CLI tools like Codex and Claude Code for terminal-based generation and refactoring.

**Q: How will you ensure a fair comparison between AI and manual coding?**
A: I have documented the exact start and end times for both sprints using WakaTime. I will use the exact same benchmark tasks and requirements for both runs to ensure the metrics are comparable.

**Q: What is the business goal of this productivity sprint?**
A: The goal is to measure the real-world impact of AI coding assistants on developer velocity and code quality, understanding both the time saved and the potential cognitive overhead.

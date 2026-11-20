# Setup Notes: Copilot Productivity Sprint

## 1. Development Environments (IDEs)
- **Primary IDE:** Visual Studio Code (VS Code)
  - Version: 1.98.2
- **Secondary Environment:** Antigravity
  - Version: 0.1.0

## 2. AI Coding Assistants
For this sprint, I installed and configured **GitHub Copilot** in VS Code as the primary AI assistant to compare against manual coding.
- **AI Assistant 1:** GitHub Copilot & Copilot Chat (VS Code Extension)
  - Version: Latest
  - Usage: Inline code generation, autocomplete, test generation, and architectural suggestions.
- **AI Assistant 2:** Codex CLI
  - Version: 0.1.0
  - Usage: Terminal-based prompt generation and boilerplate script generation.
- **AI Assistant 3:** Claude Code CLI
  - Version: 0.2.9
  - Usage: Larger refactoring tasks, explaining complex code blocks, and generating E2E tests.

## 3. VS Code Extensions & Tooling
To track productivity metrics (time and code changes) during the sprint, the following extensions and tools are installed:
- **Time Tracking:** WakaTime, Clockify (for tracking baseline vs. AI time)
- **Version Control:** Git, GitHub, GitLens
- **Testing:** Jest, React Testing Library, Pytest
- **Code Quality:** ESLint, Prettier
- **API Tools:** Postman / Thunder Client

## 4. Setup Process
1. Installed and authenticated VS Code and the Antigravity environment.
2. Installed and configured the **GitHub Copilot** extension within VS Code.
3. Installed and configured Codex CLI globally via terminal.
4. Installed and authenticated Claude Code CLI globally via terminal.
5. Disabled any other conflicting AI tab-completion tools (like Tabnine) to ensure a clean baseline for the "Series A: Development without AI" sprint.
6. Configured WakaTime to manually record start/stop times and track lines of code for the benchmark tasks.

## 5. Benchmark Task Environment
- **Language:** Python 3.12 and Node.js 20
- **Package Manager:** pip and npm
- **Testing Framework:** pytest and Jest (with >80% coverage target)

## 6. Q&A (Project Clarifications)
**Q: How will you ensure a fair comparison between Series A and Series B?**
A: I have documented the exact start and end times using WakaTime. Both sprints use the exact same benchmark tasks (Word Frequency Counter, User Registration Validator, CSV Average Calculator) and requirements.

**Q: What specific metrics are being tracked?**
A: I am tracking Time Metrics (feature development, bug fixing, testing, documentation) and Quality Metrics (code review feedback, test coverage, bug density, AI suggestion acceptance rate).

**Q: How does this tie into the business goal?**
A: The goal is to measure the real-world impact of AI coding assistants on developer velocity and code quality, understanding both the time saved and the potential cognitive overhead.

# AGENTS.md

## System Topology
This repository is a multi-agent collaborative environment. All editors must respect the following role definitions and operational boundaries.

| Agent | Domain/Role | Primary Expertise |
| :--- | :--- | :--- |
| **Me (Human)** | Architect & Reviewer | Final authority on all changes and direction. |
| **GeminiCLI** | Strategic Orchestrator | Research, planning, and high-level project management. |
| **Jules (Google)** | Asynchronous Developer | Background tasks, large-scale refactoring, and automated PRs. |
| **ClaudeCode** | Logic & Analysis | Complex reasoning, logic verification, and deep code analysis. |
| **Codex (OpenAI)** | Surgical Editor | Quick edits, boilerplate, and real-time pair programming. |
| **Antigravity** | Infrastructure & Tools | System-level tasks and automation scripts. |

## Engineering Standards
- **Style Consistency:** Adhere to existing project conventions (PEP 8 for Python, Prettier for JS/TS).
- **Test-Driven Development:** Every new feature or bug fix MUST include a corresponding test file.
- **Atomic Commits:** Keep changes focused and well-documented.

## Skills & Knowledge Base
Specialized knowledge is stored in the `/skills` directory. Agents should consult these files before implementing domain-specific logic.
- **Python MCDM/MCDA:** Refer to `/skills/mcdm.md` for mathematical models and library preferences (e.g., NumPy, SciPy, custom math).
- **Obsidian Integration:** Refer to `/skills/obsidian.md` for markdown standards and knowledge management workflows.

## Operational Boundaries
- **Permissions:** Agents may create branches and draft PRs. Only the **Human** may merge to `main`.
- **Conflicts:** If two agents propose conflicting changes, wait for **Human** resolution or **GeminiCLI** orchestration.
- **Do NOT:** Modify `.jules/`, `.gemini/`, or other tool-specific configuration folders.

#!/usr/bin/env python3
"""
This script creates the .github/copilot-instructions.md file for the projectdna-cli repository.
Run with: python setup_github_copilot_instructions.py
"""

import os
import sys
from pathlib import Path


def main():
    # Get the current working directory
    cwd = Path.cwd()
    print(f"Working directory: {cwd}")
    
    # Create .github directory
    github_dir = cwd / ".github"
    try:
        github_dir.mkdir(exist_ok=True)
        print(f"✓ Directory exists or created: {github_dir}")
    except Exception as e:
        print(f"✗ Failed to create directory: {e}", file=sys.stderr)
        return 1
    
    # Define the content
    content = """# Copilot Instructions for projectdna-cli

## Project Overview

**projectdna-cli** is a Python CLI tool built with Typer that analyzes and profiles software projects. It displays project metadata (tech stack, difficulty level, resume impact) in a structured format.

## Architecture

### Stack
- **Framework**: [Typer](https://typer.tiangolo.com/) - Modern Python CLI framework built on Click
- **Output**: [Rich](https://rich.readthedocs.io/) - Terminal formatting library for styled output
- **Entry Point**: `app.py` - Contains the Typer app instance and command definitions

### Command Structure
- Commands are defined as functions decorated with `@app.command()`
- Current command: `analyze(project: str)` - Accepts a project name and displays analysis info
- Output uses Rich `Panel` for visual formatting

## Development Setup

### Dependencies
- **typer** - CLI framework
- **rich** - Terminal output formatting

### Installation
```bash
pip install typer rich
```

### Running Commands
```bash
# Run a specific command
python app.py analyze "my-project"

# View available commands
python app.py --help

# View help for a specific command
python app.py analyze --help
```

## Key Conventions

1. **Command Definitions**: New commands should be added as functions decorated with `@app.command()` in `app.py`
2. **Output Format**: Use Rich's `Panel`, `print()`, and other formatting options for styled terminal output
3. **Parameter Typing**: Leverage Typer's support for type hints; use `str`, `int`, etc. to define CLI argument types
4. **Help Text**: Add docstrings to command functions - Typer automatically converts them to CLI help text

## File Organization

```
projectdna-cli/
├── app.py              # Main CLI application with Typer app instance
├── .github/
│   └── copilot-instructions.md  # This file
└── .venv/              # Virtual environment
```

## Testing & Validation

Currently, no automated test suite exists. Manual testing:
```bash
python app.py analyze "test-project"
```

If tests are added, they would follow a standard pytest pattern in a `tests/` directory.
"""
    
    # Write the file
    file_path = github_dir / "copilot-instructions.md"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        file_size = os.path.getsize(file_path)
        print(f"✓ File created: {file_path}")
        print(f"✓ File size: {file_size} bytes")
        return 0
    except Exception as e:
        print(f"✗ Failed to write file: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

import typer
from rich import print
from rich.panel import Panel

app = typer.Typer()

# -------- ANALYZE COMMAND --------
@app.command()
def analyze(project: str):
    prompt = f"""
Analyze this software project idea:

{project}

Give:
- Tech stack
- Difficulty level
- Resume impact
- Improvements
"""

    print(Panel.fit("[bold cyan]🧬 ProjectDNA Prompt Generated[/bold cyan]"))
    print(prompt)
    print("\n👉 Copy this prompt and paste into Copilot CLI.")

# -------- REALITY CHECK COMMAND (WOW FEATURE) --------
@app.command()
def realitycheck(idea: str):
    prompt = f"""
Evaluate this project idea honestly:

{idea}

Give:
- Originality score (1-10)
- Market saturation
- Risks
- Unique twist suggestions
"""

    print(Panel.fit("[bold magenta]🚀 ProjectDNA Reality Check[/bold magenta]"))
    print(prompt)
    print("\n👉 Copy this and paste into Copilot CLI.")

if __name__ == "__main__":
    app()

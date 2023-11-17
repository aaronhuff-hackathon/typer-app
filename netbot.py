#!/usr/bin/python3

# pypi imports
import typer
import time
from rich.progress import track

# internal imports
# from scripts import hello

__version__ = "1.0"
__author__ = "Aaron Huff"

HEADER = f"""
Netbot {__version__} by {__author__}
====================================
"""

MENU = f"""
1. Run python script.
2. Run ansible playbook.
3. Run shell script.

q - quit, h -help
"""

OPTIONS = [
    "1",
    "2",
    "3",
    "q",
    "h",
]

app = typer.Typer(
    help=f"Netbot {__version__} by {__author__}",
    add_help_option=True,
    add_completion=True,
    rich_help_panel=True,
)


@app.command(help="Run iteractive menu", rich_help_panel="Main")
def run():
    print(HEADER)
    while True:
        print(MENU)
        user_input = typer.prompt("#")
        if user_input in OPTIONS:
            print(f"Running {user_input}...")
            print("----------------------------------------------------------------")
            match user_input:
                case "q":
                    raise typer.Abort()
                case "1":
                    result = python()
                case "2":
                    result = ansible()
            print(f"{result}")
            print("----------------------------------------------------------------")
            print(f"..Done running {user_input}")
        else:
            print("Invalid option")


@app.command(
    deprecated=True, help="Sample depecreated command", rich_help_panel="DNAC"
)
def old():
    print("Don't run me")


@app.command(help="Hello python script", rich_help_panel="DNAC")
def python():
    name = typer.prompt(f"Hello, {typer.prompt('name')}")
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    return f"hello, {name}"

@app.command(help="Hello ansible playbook", rich_help_panel="DNAC")
def ansible():
    return "hello, world"


if __name__ == "__main__":
    app()

import subprocess
from pathlib import Path

from crewai.tools import tool


@tool("Terminal Runner")
def terminal_runner(project_path: str = "generated_website") -> str:
    """
    Install dependencies and start the Vite server.
    """

    project = Path(project_path)

    if not project.exists():
        return f"Project not found: {project}"

    print("\nInstalling npm packages...\n")

    subprocess.run(
        ["npm", "install"],
        cwd=project,
        shell=True
    )

    print("\nStarting Vite...\n")

    subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=project,
        shell=True
    )

    return """
==========================================
DevRaQ.ai Finished Successfully
==========================================

React Website Generated

Open:

http://localhost:5173

==========================================
"""
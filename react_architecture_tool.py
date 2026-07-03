import json
from pathlib import Path

from crewai.tools import tool


@tool("React Architecture")
def react_architecture(ui_design_file: str) -> str:
    """
    Creates the folder structure for the React website.
    """

    ui_path = Path(ui_design_file)

    if not ui_path.exists():
        return f"UI Design file not found: {ui_design_file}"

    with open(ui_path, "r", encoding="utf-8") as f:
        ui = json.load(f)

    project = Path("generated_website")

    folders = [
        project / "src",
        project / "src" / "components",
        project / "src" / "styles",
        project / "src" / "assets",
        project / "public",
        project / "data"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    files = [
        project / "src" / "App.jsx",
        project / "src" / "main.jsx",
        project / "package.json",
        project / "vite.config.js",
        project / "index.html"
    ]

    for file in files:
        if not file.exists():
            file.touch()

    components = [
        "Navbar.jsx",
        "Hero.jsx",
        "About.jsx",
        "Features.jsx",
        "Benefits.jsx",
        "Workflow.jsx",
        "Contact.jsx",
        "Footer.jsx"
    ]

    component_dir = project / "src" / "components"

    for component in components:
        (component_dir / component).touch(exist_ok=True)

    return (
        "React architecture created successfully.\n"
        f"Project Folder: {project}"
    )
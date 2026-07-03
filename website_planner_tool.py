import json
from pathlib import Path

from crewai.tools import tool


@tool("Website Planner")
def website_planner(plan_file: str) -> str:
    """
    Converts the AI generated website plan into
    a React website layout.
    """

    plan_path = Path(plan_file)

    if not plan_path.exists():
        return f"Plan file not found: {plan_file}"

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    layout = {
        "project_name": plan.get("website_name", "DevRaQ.ai"),
        "pages": [
            {
                "name": "Home",
                "route": "/",
                "components": [
                    "Navbar",
                    "Hero",
                    "About",
                    "Features",
                    "Benefits",
                    "Workflow",
                    "Contact",
                    "Footer"
                ]
            }
        ]
    }

    output_folder = Path("generated_website/data")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "website_layout.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(layout, f, indent=4)

    return (
        f"Website layout generated successfully.\n"
        f"Saved at:\n{output_file}"
    )
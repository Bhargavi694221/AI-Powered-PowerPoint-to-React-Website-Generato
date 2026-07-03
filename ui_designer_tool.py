import json
from pathlib import Path

from crewai.tools import tool


@tool("UI Designer")
def ui_designer(layout_file: str) -> str:
    """
    Creates a UI design system for the generated website.
    """

    layout_path = Path(layout_file)

    if not layout_path.exists():
        return f"Layout file not found: {layout_file}"

    with open(layout_path, "r", encoding="utf-8") as f:
        layout = json.load(f)

    ui_design = {
        "theme": {
            "primary": "#2563EB",
            "secondary": "#7C3AED",
            "background": "#F8FAFC",
            "text": "#1E293B",
            "accent": "#06B6D4"
        },

        "typography": {
            "font": "Poppins",
            "heading": "48px",
            "subheading": "32px",
            "body": "18px"
        },

        "navbar": {
            "sticky": True,
            "transparent": False
        },

        "hero": {
            "animation": "fade-up",
            "button_style": "gradient"
        },

        "cards": {
            "border_radius": "16px",
            "shadow": "large"
        },

        "footer": {
            "dark": True
        },

        "pages": layout["pages"]
    }

    output_folder = Path("generated_website/data")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "ui_design.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(ui_design, f, indent=4)

    return (
        "UI Design created successfully.\n"
        f"Saved at:\n{output_file}"
    )
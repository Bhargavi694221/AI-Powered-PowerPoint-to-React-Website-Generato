import json
from pathlib import Path
from crewai.tools import tool


@tool("Knowledge Extractor")
def knowledge_extractor(json_file: str) -> str:
    """
    Reads website_content.json and extracts structured knowledge.
    """

    json_path = Path(json_file)

    if not json_path.exists():
        return f"JSON not found: {json_file}"

    with open(json_path, "r", encoding="utf-8") as f:
        slides = json.load(f)

    website_knowledge = {
        "website_title": "",
        "sections": [],
        "features": [],
        "benefits": [],
        "technologies": [],
        "workflow": []
    }

    # If JSON is a dictionary, get slides
    if isinstance(slides, dict):
        slides = slides.get("slides", [])

    # If JSON is a list, use it directly
    if not isinstance(slides, list):
        return "Invalid JSON format."

    if len(slides) > 0:
        website_knowledge["website_title"] = slides[0].get("title", "DevRaQ.ai")

    for slide in slides:

        title = slide.get("title", "")

        website_knowledge["sections"].append(title)

        texts = (
            slide.get("texts")
            or slide.get("content")
            or []
        )

        for text in texts:

            text_lower = text.lower()

            if "feature" in text_lower:
                website_knowledge["features"].append(text)

            if "benefit" in text_lower:
                website_knowledge["benefits"].append(text)

            if (
                "react" in text_lower
                or "python" in text_lower
                or "vite" in text_lower
            ):
                website_knowledge["technologies"].append(text)

            if (
                "workflow" in text_lower
                or "phase" in text_lower
            ):
                website_knowledge["workflow"].append(text)

    output_folder = Path("generated_website/data")
    output_folder.mkdir(parents=True, exist_ok=True)

    knowledge_file = output_folder / "knowledge.json"

    with open(knowledge_file, "w", encoding="utf-8") as f:
        json.dump(
            website_knowledge,
            f,
            indent=4,
            ensure_ascii=False
        )

    return (
        "Knowledge extracted successfully.\n"
        f"Saved at:\n{knowledge_file}"
    )
import json
from pathlib import Path

from crewai import LLM
from crewai.tools import tool


# Configure your LLM
llm = LLM(
    model="qwen2.5-vl-72b",
    base_url="http://192.168.100.138:8000/v1",
    api_key="dummy"
)


@tool("AI Content Understanding")
def ai_content_understanding(knowledge_file: str) -> str:
    """
    Uses an LLM to understand the extracted PPT knowledge
    and generate a modern website plan.
    """

    knowledge_path = Path(knowledge_file)

    if not knowledge_path.exists():
        return f"Knowledge file not found: {knowledge_file}"

    with open(knowledge_path, "r", encoding="utf-8") as f:
        knowledge = json.load(f)

    prompt = f"""
You are an expert UI/UX Designer and React Developer.

Below is the extracted knowledge from a PowerPoint.

{json.dumps(knowledge, indent=2)}

Your job is to understand the presentation.

Do NOT copy slide text.

Instead, create a professional modern SaaS website.

Return ONLY valid JSON.

Do NOT write explanations.

Do NOT use markdown.

Return exactly this format:

{{
    "website_name": "",
    "hero": {{
        "title": "",
        "subtitle": "",
        "button": ""
    }},
    "about": "",
    "features": [
        "...",
        "...",
        "..."
    ],
    "benefits": [
        "...",
        "...",
        "..."
    ],
    "workflow": [
        "...",
        "...",
        "..."
    ],
    "contact": {{
        "email": "",
        "phone": ""
    }}
}}
"""

    # Call the LLM
    response = llm.call(prompt)

    # Remove markdown code fences if present
    response = response.strip()

    if response.startswith("```json"):
        response = response[len("```json"):]

    if response.startswith("```"):
        response = response[3:]

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    output_folder = Path("generated_website/data")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "website_plan.json"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response)

    return (
        "✅ Website plan generated successfully.\n"
        f"Saved at:\n{output_file}"
    )
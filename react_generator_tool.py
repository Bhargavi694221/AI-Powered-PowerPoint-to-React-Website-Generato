import json
from pathlib import Path

from crewai.tools import tool


@tool("React Generator")
def react_generator(plan_file: str) -> str:
    """
    Generate React components from website_plan.json
    """

    plan_path = Path(plan_file)

    if not plan_path.exists():
        return f"Website plan not found: {plan_file}"

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    components = Path("generated_website/src/components")
    components.mkdir(parents=True, exist_ok=True)

    # ---------------- HERO ----------------

    hero = f'''export default function Hero() {{
    return (
        <section className="hero">
            <h1>{plan["hero"]["title"]}</h1>
            <p>{plan["hero"]["subtitle"]}</p>
            <button>{plan["hero"]["button"]}</button>
        </section>
    );
}}
'''

    (components / "Hero.jsx").write_text(hero, encoding="utf-8")

    # ---------------- ABOUT ----------------

    about = f'''export default function About() {{
    return (
        <section className="about">
            <h2>About</h2>
            <p>{plan["about"]}</p>
        </section>
    );
}}
'''

    (components / "About.jsx").write_text(about, encoding="utf-8")

    # ---------------- FEATURES ----------------

    feature_items = "\n".join(
        [f"<li>{item}</li>" for item in plan["features"]]
    )

    features = f'''export default function Features() {{
    return (
        <section className="features">
            <h2>Features</h2>
            <ul>
                {feature_items}
            </ul>
        </section>
    );
}}
'''

    (components / "Features.jsx").write_text(features, encoding="utf-8")

    # ---------------- BENEFITS ----------------

    benefit_items = "\n".join(
        [f"<li>{item}</li>" for item in plan["benefits"]]
    )

    benefits = f'''export default function Benefits() {{
    return (
        <section className="benefits">
            <h2>Benefits</h2>
            <ul>
                {benefit_items}
            </ul>
        </section>
    );
}}
'''

    (components / "Benefits.jsx").write_text(benefits, encoding="utf-8")

    # ---------------- WORKFLOW ----------------

    workflow_items = "\n".join(
        [f"<li>{item}</li>" for item in plan["workflow"]]
    )

    workflow = f'''export default function Workflow() {{
    return (
        <section className="workflow">
            <h2>Workflow</h2>
            <ol>
                {workflow_items}
            </ol>
        </section>
    );
}}
'''

    (components / "Workflow.jsx").write_text(workflow, encoding="utf-8")

    # ---------------- CONTACT ----------------

    contact = f'''export default function Contact() {{
    return (
        <section className="contact">
            <h2>Contact</h2>
            <p>Email: {plan["contact"]["email"]}</p>
            <p>Phone: {plan["contact"]["phone"]}</p>
        </section>
    );
}}
'''

    (components / "Contact.jsx").write_text(contact, encoding="utf-8")

    return "React Components Generated Successfully."
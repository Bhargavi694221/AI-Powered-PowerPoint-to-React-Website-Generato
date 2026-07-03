from crewai import Task


def create_tasks(
    ppt_agent,
    image_agent,
    content_agent,
    react_agent,
    app_agent,
    terminal_agent,
):
    ppt_task = Task(
        description="""
        Read the PowerPoint presentation located at
        knowledge/DevRaQ.pptx
        """,
        expected_output="List of slides and titles.",
        agent=ppt_agent,
    )

    image_task = Task(
        description="""
        Extract every embedded image from the PowerPoint and save
        them into generated_website/assets.
        """,
        expected_output="Images extracted successfully.",
        agent=image_agent,
    )

    content_task = Task(
        description="""
        Analyze the PowerPoint and generate
        generated_website/data/website_content.json.
        """,
        expected_output="JSON file created.",
        agent=content_agent,
    )

    react_task = Task(
        description="""
        Generate React components using
        website_content.json.
        """,
        expected_output="React components created.",
        agent=react_agent,
    )

    app_task = Task(
        description="""
        Generate App.jsx that imports every
        React component.
        """,
        expected_output="App.jsx created.",
        agent=app_agent,
    )

    terminal_task = Task(
        description="""
        Install npm packages and run the
        Vite development server.
        """,
        expected_output="React website running.",
        agent=terminal_agent,
    )

    return [
        ppt_task,
        image_task,
        content_task,
        react_task,
        app_task,
        terminal_task,
    ]
from crewai import Agent

from devraq_website.tools.ppt_reader_tool import ppt_reader
from devraq_website.tools.image_extractor_tool import image_extractor
from devraq_website.tools.content_analyzer_tool import content_analyzer
from devraq_website.tools.react_generator_tool import react_generator
from devraq_website.tools.component_generator_tool import component_generator
from devraq_website.tools.app_generator_tool import app_generator
from devraq_website.tools.terminal_tool import terminal_runner


def create_agents(llm):

    ppt_agent = Agent(
        role="PowerPoint Reader",
        goal="Read PowerPoint presentations.",
        backstory="Expert in python-pptx.",
        tools=[ppt_reader],
        llm=llm,
        verbose=True,
    )

    image_agent = Agent(
        role="Image Extractor",
        goal="Extract images from PowerPoint.",
        backstory="Expert in image extraction.",
        tools=[image_extractor],
        llm=llm,
        verbose=True,
    )

    content_agent = Agent(
        role="Content Analyzer",
        goal="Convert PowerPoint into structured JSON.",
        backstory="Expert in document analysis.",
        tools=[content_analyzer],
        llm=llm,
        verbose=True,
    )

    react_agent = Agent(
        role="React Generator",
        goal="Generate React components.",
        backstory="Senior React developer.",
        tools=[react_generator, component_generator],
        llm=llm,
        verbose=True,
    )

    app_agent = Agent(
        role="App Generator",
        goal="Generate App.jsx.",
        backstory="React architect.",
        tools=[app_generator],
        llm=llm,
        verbose=True,
    )

    terminal_agent = Agent(
        role="Terminal Runner",
        goal="Run Vite.",
        backstory="Automation expert.",
        tools=[terminal_runner],
        llm=llm,
        verbose=True,
    )

    return (
        ppt_agent,
        image_agent,
        content_agent,
        react_agent,
        app_agent,
        terminal_agent,
    )
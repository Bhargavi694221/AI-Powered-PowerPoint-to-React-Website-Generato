from crewai import Crew, Process, LLM

from devraq_website.agents import create_agents
from devraq_website.tasks import create_tasks


# Configure LLM
llm = LLM(
    MODEL="qwen2.5-vl-72b",
    BASE_URL="http://192.168.100.138:8000/v1",
    API_KEY="dummy",
)


def create_crew():

    (
        ppt_agent,
        image_agent,
        content_agent,
        react_agent,
        app_agent,
        terminal_agent,
    ) = create_agents(llm)

    tasks = create_tasks(
        ppt_agent,
        image_agent,
        content_agent,
        react_agent,
        app_agent,
        terminal_agent,
    )

    crew = Crew(
        agents=[
            ppt_agent,
            image_agent,
            content_agent,
            react_agent,
            app_agent,
            terminal_agent,
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    return crew
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

news_agent = Agent(
    name='A Basic Agent',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    description="You are a news reporter that reports the news in three lines in simple language with date of news.",
    markdown=True
)

news_agent.print_response("Give me the latest news about political breakdown going on in usa with the web url link.")
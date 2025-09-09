from agno.models.google import Gemini
from agno.agent import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    reasoning=True
)

agent.print_response("How much time does it required for a person to travel from lahore to islamabad on feets.",
                     steam=True)
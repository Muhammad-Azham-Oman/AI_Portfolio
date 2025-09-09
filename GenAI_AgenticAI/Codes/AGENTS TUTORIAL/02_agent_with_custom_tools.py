from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def custom_tool(company_name):
    """
    Use this function to get the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol.

    Returns:
        str: The current stock price or error message.
    """
    symbols={
        "Azham": "AAPL",
        "Bahia": "BAH",
        "Bangkok": "BANK"
    }
    return symbols.get(company_name, company_name)

news_agent = Agent(
    name='Agent with some tools',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools(),custom_tool,YFinanceTools(stock_price= True,
                                           company_info= True,
                                           stock_fundamentals = True,
                                           income_statements = True,
                                           analyst_recommendations= True),
    ],
    instructions=[
        "Use tables to display data",
        "Don't use the custom tool if you get the stock symbol by company name on your own, use it only when you don't get the stock name from your knowledge."
    ],
    show_tool_calls=True,
    markdown=True
)

news_agent.print_response("What is the stock price of Azham.")
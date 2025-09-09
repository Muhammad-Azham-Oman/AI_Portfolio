from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=
    [ReasoningTools(add_instructions=True),
     YFinanceTools(
        stock_price = True,
        company_info = True,
        stock_fundamentals = True,
        income_statements = True,
        key_financial_ratios = True,
        analyst_recommendations = True,
        company_news = True,
        technical_indicators = True,
        historical_prices = True,
        enable_all = True)],

    instructions=[
        "Use tables to extract data and display data.",
        "Only give the output no other text"
    ],
    markdown=True
)

agent.print_response("Write the report on Nvidia.")
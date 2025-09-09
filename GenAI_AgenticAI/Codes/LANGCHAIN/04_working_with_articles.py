from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

prompt = '''
From the bellow news articale extract revenue and eps in JSON format containing the these keys :
revenue_actual , revenue_expected , eps_actual , eps-expected

Only return the JSON no preamble

Article
======
{Article}
======
'''

pt = PromptTemplate.from_template(prompt)


llm = ChatGroq(model='llama-3.3-70b-versatile')

chain = pt | llm

article = '''
Apple
 reported third-quarter earnings on Thursday that topped Wall Street expectations for profit and revenue.

iPhone sales grew 13% year over year and overall revenue grew 10% — Apple’s largest quarterly revenue growth since December 2021.

Apple shares rose in after-hours trading on Thursday and took a leg higher after Apple provided data points about the company’s performance in the September quarter.

Here’s how Apple did versus consensus estimates for the quarter ending June 28:

Earnings per share: $1.57 vs. $1.43 expected
Revenue: $94.04 billion vs. $89.53 billion expected'''

output = chain.invoke({'Article' : article})
print(type(output.content))
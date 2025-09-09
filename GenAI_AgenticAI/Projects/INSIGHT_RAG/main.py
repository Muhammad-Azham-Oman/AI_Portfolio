import gradio as gr
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGroq(model='llama3-70b-8192')  # Or your available model name

# Function to extract financial data using LangChain
def extract_financial_data(text):
    prompt = '''
    From the below news article extract revenue and EPS in JSON format with these keys:
    revenue_actual, revenue_expected, eps_actual, eps_expected

    Include proper units (like millions, billions, dollars, cents, etc.) in the values with signs.

    Only return the JSON. No explanation or preamble.

    Article:
    ======
    {text}
    ======
    '''

    try:
        # Prepare the chain
        pt = PromptTemplate.from_template(prompt)
        chain = pt | llm

        # Run chain
        output = chain.invoke({'text': text})  # key must match template var
        parser = JsonOutputParser()
        output_json = parser.parse(output.content)

        # Convert to formatted DataFrame
        df = pd.DataFrame([
            {
                "Measure": "Revenue",
                "Estimated": output_json.get("revenue_expected", "N/A"),
                "Actual": output_json.get("revenue_actual", "N/A")
            },
            {
                "Measure": "EPS",
                "Estimated": output_json.get("eps_expected", "N/A"),
                "Actual": output_json.get("eps_actual", "N/A")
            }
        ])
        return df

    except OutputParserException as e:
        return pd.DataFrame([{"Measure": "Error", "Estimated": "Parser failed", "Actual": str(e)}])
    except Exception as e:
        return pd.DataFrame([{"Measure": "Error", "Estimated": "General failure", "Actual": str(e)}])
# Luxurious CSS
css = """
h1 {
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
    color: #ffffff;
    font-size: 2.5rem;
    margin-bottom: 30px;
}

textarea {
    font-family: 'Courier New', monospace;
    font-size: 1rem;
}

.gradio-container {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
    padding: 40px;
    min-height: 100vh;
}

button {
    background-color: #00c6ff;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0072ff;
}
"""

# Gradio Interface
with gr.Blocks(css=css, theme=gr.themes.Base()) as app:
    gr.Markdown("# FINANCIAL DATA EXTRACTION")

    with gr.Row():
        input_text = gr.Textbox(label="Enter Financial Text", lines=6, placeholder="Paste your financial news article here...")

    extract_button = gr.Button("Extract")

    output_table = gr.Dataframe(headers=["Measure", "Estimated", "Actual"], interactive=False)

    extract_button.click(fn=extract_financial_data, inputs=input_text, outputs=output_table)

app.launch()
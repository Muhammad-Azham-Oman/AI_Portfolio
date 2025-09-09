from agno.models.google import Gemini
from agno.agent import Agent
from dotenv import load_dotenv
from agno.media import Image
from pathlib import Path

load_dotenv()

def get_item_code(item_name):
    """
    Returns the item code corresponding to the provided item name. If the item
    name does not match any predefined items, a default code is returned.

    :param item_name: The name of the item to retrieve the code for. Expected
                      values are "dress", "t-shirt", "jeans", "jacket".
    :type item_name: str
    :return: The code corresponding to the given item name. Returns "ITM001"
             for "dress", "ITM002" for "t-shirt", "ITM003" for "jeans",
             "ITM004" for "jacket", and "ITM999" for any other input.
    :rtype: str
    """
    if item_name == "dress":
        return "ITM001"

    if item_name == "t-shirt":
        return "ITM002"

    if item_name == "jeans":
        return "ITM003"

    if item_name == "jacket":
        return "ITM004"

    return "ITM999"


agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[get_item_code]
)

response = agent.run(
    message='''
    For each image create a Json record that lot exact like this:
    {
        "item_name": "shirt",
        "item_code": "ITM001",
        "color": "red",
        "gender": "male",
        "age_category": "adult" 
    }
    :type item_name: json
    Output must be a JSON strings that Python can parse it directly.
    don't never ever give the output in string or with any preambles just a fine Json string as shown above.
    Do not put any pre-amble instructions or event like 'json' or ```json in front of the response string.
    Just the {} in which there is the requirement as shown above.
    item_name should be one of the following: dress, t-shirt, jeans, jacket
    age_category should be one of the following: adult, child.
    give the item_code as per the item.
    ''',
    images=
    [
        Image(filepath=Path(__file__).parent / "images" / "image1.jpg"),
        Image(filepath=Path(__file__).parent / "images" / "image2.jpg"),
        Image(filepath=Path(__file__).parent / "images" / "image3.jpg"),
        Image(filepath=Path(__file__).parent / "images" / "image4.jpg"),
        Image(filepath=Path(__file__).parent / "images" / "image5.jpg"),
    ]
)

print(response.content)
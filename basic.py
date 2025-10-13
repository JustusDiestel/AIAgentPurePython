import os
from openai import OpenAI
from dotenv import load_dotenv
from pydentic import BaseModel
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

prompt = input("Bitte gib deinen Prompt ein: ")

response = client.responses.create(
    model ="gpt-5-nano",
    input =prompt,
    store =True,
)


print(response.output_text)


class CalenderEvent(BaseModel):
    name: str
    date: str
    participants: List[str]
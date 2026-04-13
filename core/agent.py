from groq import Groq
from utils.config import GROQ_API_KEY, MODEL_NAME

class Agent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def run(self, messages):
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )
        return response.choices[0].message.content
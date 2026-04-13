from groq import Groq
from utils.config import GROQ_API_KEY, MODEL_NAME
import json

SYSTEM_PROMPT = """
You are IGRIS, an AI assistant with tool access.

STRICT RULES:
- You MUST use tools when a task involves real-world actions
- DO NOT explain manual steps if a tool can do it
- DO NOT suggest terminal commands
- ALWAYS respond in JSON

Available tools:
- open_notepad: Opens Notepad
- open_google: Opens Google in browser
- open_website: Opens a website URL

Response format:

Normal:
{
  "type": "response",
  "content": "text"
}

Tool:
{
  "type": "tool",
  "tool_name": "exact tool name",
  "input": "optional"
}
"""

class Agent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def run(self, messages):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except:
            return {
                "type": "response",
                "content": content
            }
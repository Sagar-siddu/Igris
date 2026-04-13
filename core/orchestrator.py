from core.agent import Agent
from memory.short_term import ShortTermMemory
from tools.system_tools import OpenNotepadTool

class Orchestrator:
    def __init__(self):
        self.agent = Agent()
        self.memory = ShortTermMemory()
        self.tools = {
            "open_notepad": OpenNotepadTool()
        }

    def handle(self, user_input):
        # Tool trigger (basic rule-based for now)
        if "open notepad" in user_input.lower():
            return self.tools["open_notepad"].run(user_input)

        # Add user input to memory
        self.memory.add("user", user_input)

        # Get response from LLM
        messages = self.memory.get()
        response = self.agent.run(messages)

        # Store response
        self.memory.add("assistant", response)

        return response
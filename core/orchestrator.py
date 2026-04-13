from core.agent import Agent
from memory.short_term import ShortTermMemory
from tools.system_tools import OpenNotepadTool, OpenGoogleTool, OpenWebsiteTool

class Orchestrator:
    def __init__(self):
        self.agent = Agent()
        self.memory = ShortTermMemory()

        self.tools = {
            "open_notepad": OpenNotepadTool(),
            "open_google": OpenGoogleTool(),
            "open_website": OpenWebsiteTool()
        }

    def handle(self, user_input):
        self.memory.add("user", user_input)

        messages = self.memory.get()
        decision = self.agent.run(messages)

        # CASE 1: Normal response
        if decision["type"] == "response":
            response = decision["content"]
            self.memory.add("assistant", response)
            return response

        # CASE 2: Tool call
        elif decision["type"] == "tool":
            tool_name = decision["tool_name"]

            if tool_name not in self.tools:
                return "I don't know how to do that yet."

            tool = self.tools[tool_name]
            tool_result = tool.run(decision.get("input", ""))

            # Feed result back to LLM for final response
            self.memory.add("assistant", f"Tool result: {tool_result}")

            final = self.agent.run(self.memory.get())

            if final["type"] == "response":
                self.memory.add("assistant", final["content"])
                return final["content"]

            return str(final)
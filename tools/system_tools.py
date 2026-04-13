import os
from tools.base_tool import BaseTool

class OpenNotepadTool(BaseTool):
    name = "open_notepad"
    description = "Opens notepad"

    def run(self, input_text):
        os.system("notepad")
        return "Opened Notepad"
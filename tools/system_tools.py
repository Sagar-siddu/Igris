import os
import webbrowser
from tools.base_tool import BaseTool

class OpenNotepadTool(BaseTool):
    name = "open_notepad"
    description = "Opens Notepad application"

    def run(self, input_text):
        os.system("notepad")
        return "Notepad opened"


class OpenGoogleTool(BaseTool):
    name = "open_google"
    description = "Opens Google in browser"

    def run(self, input_text):
        webbrowser.open("https://www.google.com")
        return "Opened Google"

class OpenWebsiteTool(BaseTool):
    name = "open_website"
    description = "Opens a given website URL in browser"

    def run(self, input_text):
        webbrowser.open(input_text)
        return f"Opened {input_text}"    
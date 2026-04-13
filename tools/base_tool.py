class BaseTool:
    name = ""
    description = ""

    def run(self, input_text: str) -> str:
        raise NotImplementedError
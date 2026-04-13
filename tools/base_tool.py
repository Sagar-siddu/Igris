class BaseTool:
    name = "base"
    description = "Base tool"

    def run(self, input_text):
        raise NotImplementedError
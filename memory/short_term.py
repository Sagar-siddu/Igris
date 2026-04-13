class ShortTermMemory:
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history

    def add(self, role, content):
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get(self):
        return self.history
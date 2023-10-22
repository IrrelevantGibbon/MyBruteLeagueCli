from typing import Any


class ContextManager:
    def __init__(self):
        self.__context = {}

    def add_context(self, name: str, value: Any):
        self.__context[name] = value

    def get_context(self, name: str) -> Any:
        return self.__context.get(name)

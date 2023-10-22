from commands_manager import CommandsManager
from context_manager import ContextManager

class Cli:
    def __init__(self):
        self.__context_manager = ContextManager()
        self.__commands_manager = CommandsManager(self.__context_manager)

    def run(self):
        while True:
            line = input("> ")
            self.__commands_manager.get_line(line)

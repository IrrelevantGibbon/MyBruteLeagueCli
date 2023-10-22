from commands_manager import CommandsManager
from context_manager import ContextManager
from file_manager import FileManager


class Cli:
    def __init__(self):
        self.__context_manager = ContextManager()
        self.__file_manager = FileManager()
        self.__commands_manager = CommandsManager(
            self.__context_manager, self.__file_manager
        )

    def run(self):
        while True:
            line = input("> ")
            self.__commands_manager.get_line(line)

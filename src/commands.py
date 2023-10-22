from typing import Dict, List, Any
from context_manager import ContextManager
from league import League


class Commands:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.ask_context = False

    def parse_args(self, args: str):
        pass

    def run(self, datas: str | None = None):
        pass

    def run(self) -> None:
        pass


class CreateLeague(Commands):
    def __init__(self, commands: Dict[str, Commands]):
        super().__init__("Create", "Create a my brute League")
        self.commands = commands
        self.name: str | None = None
        self.ask_context = True

    def parse_args(self, args: List[Any]) -> None:
        if len(args) == 0:
            return self.error()
        self.name = args[0]

    def run(self, context_manager: ContextManager) -> None:
        league = League(self.name, [])
        context_manager.add_context("league", league)

    def error(self) -> None:
        print("Error: No name given for the league")


class HelpCommands(Commands):
    def __init__(self, commands: Dict[str, Commands]):
        super().__init__("Help", "Show this help message")
        self.commands = commands

    def run(self) -> None:
        for command in self.commands.values():
            print(f"{command.name}: {command.description}")


class QuitCommands(Commands):
    def __init__(self):
        super().__init__("Quit", "Quit the program")

    def run(self) -> None:
        quit()

from typing import Dict, List, Any
from context_manager import ContextManager
from file_manager import FileManager
from league import League


class Commands:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def parse_args(self, args: str):
        pass

    def run(self, *args, **kwargs) -> None:
        pass


class LeagueCommands(Commands):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.l_name: str | None = None

    def parse_args(self, args: List[Any]) -> None:
        if len(args) == 0:
            return self.error()
        self.l_name = args[0]

    def error(self) -> None:
        print("Error: No name given for the league")


class CreateLeagueCommands(LeagueCommands):
    def __init__(self):
        super().__init__("Create", "Create a my brute League")

    def run(self, context_manager: ContextManager) -> None:
        league = League(self.l_name, [])
        context_manager.add_context("league", league)
        print(f"League {self.l_name} created")


class SaveLeagueCommands(Commands):
    def __init__(self):
        super().__init__("Save", "Save a my brute League")

    def run(self, context_manager: ContextManager, file_manager: FileManager) -> None:
        league: League = context_manager.get_context("league")
        file_manager.write_file(league.name, league)
        print(f"League {league.name} saved")


class LoadLeagueCommands(LeagueCommands):
    def __init__(self):
        super().__init__("Load", "Load a my brute League")

    def run(self, context_manager: ContextManager, file_manager: FileManager) -> None:
        context_manager.add_context("league", file_manager.read_file(self.l_name))
        print(f"League {self.l_name} loaded")


class CurrentLeagueCommands(Commands):
    def __init__(self):
        super().__init__("Current", "Current a my brute League")

    def run(self, context_manager: ContextManager) -> None:
        league: League = context_manager.get_context("league")
        if league is not None:
            print(f"Current league is {league.name}")
        else:
            print("No League selected")


class ListLeagueCommands(Commands):
    def __init__(self):
        super().__init__("List", "List all Leagues")

    def run(self, file_manager: FileManager) -> None:
        leagues = file_manager.list_files()
        if len(leagues) == 0:
            print("No League created")

        for league in leagues:
            print(league)


class DeleteLeagueCommands(LeagueCommands):
    def __init__(self):
        super().__init__("Delete", "Delete a my brute League")

    def run(self, context_manager: ContextManager, file_manager: FileManager) -> None:
        league = context_manager.get_context("league")
        if league is None:
            print("No League selected")
            return
        file_manager.delete_file(league.name)
        del league
        print("League deleted")


class AddBruteCommands(Commands):
    def __init__(self):
        super().__init__("Add", "Add a brute to a League")
        self.brute_names: List[str] = []

    def parse_args(self, args: List[Any]) -> None:
        if len(args) == 0:
            return self.error()
        self.brute_names = [name for name in args[0].split(",")]

    def run(self, context_manager: ContextManager) -> None:
        league: League = context_manager.get_context("league")
        if league is None:
            print("No League selected")
            return
        for name in self.brute_names:
            league.add_gladiator(name)
            print(f"Added {name} to {league.name}")

    def error(self) -> None:
        print("Error: No name given for the brute")


class RankingBruteLeagueCommands(Commands):
    def __init__(self):
        super().__init__("Ranking", "Ranking a my brute League")

    def run(self, context_manager: ContextManager) -> None:
        league: League = context_manager.get_context("league")
        if league is None:
            print("No League selected")
            return
        league.print_ranking()
        
class FightBruteLeagueCommands(Commands):
    def __init__(self):
        super().__init__("Fight", "Fight a my brute League")
        self.fight_number: int = 1
    
    def parse_args(self, args: List[Any]) -> None:
        if len(args) == 0 and args[0].isdigit():
            return self.error()
        self.fight_number = int(args[0])
        
    def run(self, context_manager: ContextManager) -> None:
        league: League = context_manager.get_context("league")
        if league is None:
            print("No League selected")
            return
        for _ in range(self.fight_number):
            league.fight()
        league.print_ranking()
        
    def error(self) -> None:
        print("Error: No number given for the fight")

class HelpCommands(Commands):
    def __init__(self, commands: Dict[str, Commands]):
        super().__init__("Help", "Show this help message")
        self.commands = commands

    def run(self) -> None:
        print("Available commands:\n")
        for command in self.commands.values():
            print(f"    {command.name}: {command.description}")


class QuitCommands(Commands):
    def __init__(self):
        super().__init__("Quit", "Quit the program")

    def run(self) -> None:
        print("Goodbye")
        quit()

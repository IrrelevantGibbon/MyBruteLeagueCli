from typing import Dict, List
from commands import (
    AddBruteCommands,
    ClearCommands,
    Commands,
    FightBruteLeagueCommands,
    HelpCommands,
    ListLeagueCommands,
    QuitCommands,
    CreateLeagueCommands,
    LoadLeagueCommands,
    CurrentLeagueCommands,
    DeleteLeagueCommands,
    RankingBruteLeagueCommands,
    SaveLeagueCommands,
    ShowBruteLeagueCommands,
)
from context_manager import ContextManager
from file_manager import FileManager
import inspect


class CommandNotFound(Exception):
    message = "Command {} not found"

    def __init__(self, command: str):
        super().__init__(self.message.format(command))


class CommandsManager:
    def __init__(self, context_manager: ContextManager, file_manager: FileManager):
        self.commands: List[Commands] = []
        self.context_manager = context_manager
        self.file_manager = file_manager
        self.add_base_commands()

    def add_base_commands(self):
        self.add_command(CreateLeagueCommands())
        self.add_command(LoadLeagueCommands())
        self.add_command(SaveLeagueCommands())
        self.add_command(CurrentLeagueCommands())
        self.add_command(ListLeagueCommands())
        self.add_command(DeleteLeagueCommands())
        self.add_command(AddBruteCommands())
        self.add_command(ShowBruteLeagueCommands())
        self.add_command(FightBruteLeagueCommands())
        self.add_command(RankingBruteLeagueCommands())
        self.add_command(ClearCommands())
        self.add_command(HelpCommands(self.commands))
        self.add_command(QuitCommands())

    def add_command(self, command: Commands):
        self.commands[command.name] = command
        self.commands.append(command)

    def get_line(self, line: str):
        line = line.strip()
        command_name = line.split(" ")[0]
        command_args = line.split(" ")[1:]
        self.call_commands(command_name, command_args)

    def get_commands_from_name(self, command: str) -> Commands | None:
        for c in self.commands:
            if command in c.command_names:
                return c
        return None

    def call_commands(self, command_name: str, data: str | None = None) -> None:
        command: Commands | None = self.get_commands_from_name(command_name)
        if command is not None:
            command.parse_args(data)
            command.run(**self.injects_parameters(command))
        else:
            print(f"Command {command} not found")

    def injects_parameters(self, command: Commands) -> Dict[str, any]:
        params = inspect.signature(command.run).parameters
        args = {}
        if "context_manager" in params:
            args["context_manager"] = self.context_manager
        if "file_manager" in params:
            args["file_manager"] = self.file_manager
        return args

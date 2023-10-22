from typing import Dict, Callable
from commands import (
    Commands,
    HelpCommands,
    ListLeagueCommands,
    QuitCommands,
    CreateLeagueCommands,
    LoadLeagueCommands,
    CurrentLeagueCommands,
    DeleteLeagueCommands,
    SaveLeagueCommands,
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
        self.commands: Dict[str, Commands] = {}
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
        self.add_command(HelpCommands(self.commands))
        self.add_command(QuitCommands())

    def add_command(self, command: Commands):
        self.commands[command.name] = command

    def get_line(self, line: str):
        line = line.strip()
        command_name = line.split(" ")[0]
        command_args = line.split(" ")[1:]
        self.call_commands(command_name, command_args)

    def call_commands(self, command: str, data: str | None = None):
        if command in self.commands:
            self.commands[command].parse_args(data)
            args = self.injects_parameters(self.commands[command])
            self.commands[command].run(**args)
        else:
            print(f"Command {command} not found")

    def injects_parameters(self, command: str):
        params = inspect.signature(command.run).parameters
        args = {}
        if "context_manager" in params:
            args["context_manager"] = self.context_manager
        if "file_manager" in params:
            args["file_manager"] = self.file_manager
        return args

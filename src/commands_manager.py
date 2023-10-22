from typing import Dict, Callable
from commands import Commands, HelpCommands, QuitCommands
from context_manager import ContextManager


class CommandNotFound(Exception):
    message = "Command {} not found"

    def __init__(self, command: str):
        super().__init__(self.message.format(command))


class CommandsManager:
    def __init__(self, context_manager: ContextManager):
        self.commands: Dict[str, Commands] = {}
        self.add_base_commands()

    def add_base_commands(self):
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
            if self.commands[command].ask_context:
                self.commands[command].run(self.context_manager)
            else:
                self.commands[command].run()
        else:
            print(f"Command {command} not found")

from command.source.command import Command
from command.echocommand import EchoCommand
from command.source.commandexception import CommandException


class Interpreter:
    """Custom class for interpreting a command."""

    def __init__(self):
        """Initialize a new instance of Interpreter class."""
        self.COMMANDS: dict[str, Command] = {}
        self.add_command("echo", EchoCommand())

    def add_command(self, name: str, command: Command):
        """
        Add a command to the interpreter.;
        :param name: The name with which we want to call the command.;
        :param command: The command to add.;
        """
        if name not in self.COMMANDS:
            self.COMMANDS[name] = command

    def interpret(self, command: [str]):
        """
        Method that interpret a command.;
        :param command: The command to interpret.;
        """
        # Retrieve the command name.
        command.pop(0)

        # Check the command
        if len(command) == 0:
            raise CommandException("You must type a command name")

        command_name = self.check_command(command.pop(0))
        self.COMMANDS[command_name].execute(command)

    def check_command(self, command_name: str):
        """
        Check if the command
        :param command_name: The command name.;
        :return str: The command name.;
        :raise CommandException: If the command name is not found in the command's interpreter.
        """
        if not (command_name in self.COMMANDS.keys()):
            raise CommandException("The command '" + command_name + "' unknown.")

        return command_name

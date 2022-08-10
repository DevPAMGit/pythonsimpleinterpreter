from abc import ABC

from command.source.command import Command


class EchoCommand(Command, ABC):
    """
    Basic command that print on the standard output a command.
    """

    def __init__(self):
        """
        Initialize a new instance of EchoCommand class.
        """
        super(EchoCommand, self).__init__(1)

    def check_args_type(self, args: [str]):
        """
        Check the arguments command.;
        :param args: The arguments to check.;
        :return: True if the arguments in parameter are valid; otherwise False.
        """
        return True

    def execution(self, arg: str):
        """
        Execution of the command.;
        :param arg: The command argument. ;
        """
        print(arg[0])

from abc import ABC, abstractmethod

from commandexception import CommandException


class Command(ABC):
    """Custom class for an interpreter command."""

    def __init__(self, nb_args: (int | None)):
        """
        Initialize a new instance of Command class.;
        :param nb_args: The number of arguments the command need.
        """
        self.NB_ARGS: (int | None) = nb_args

    def check_nb_arguments(self, nb_args: int) -> bool:
        """
        Check the number of arguments is good.;
        :param nb_args: The number of arguments.;
        :return: True if the number of arguments is the same of what expected.
        """
        if self.NB_ARGS is None:
            return True
        return self.NB_ARGS == nb_args

    def execute(self, args: [str]):
        """
        Execute the command with the arguments in parameter.;
        :param args: The command arguments.
        :raise: CommandException If the number of arguments or their type is invalid.
        """
        if not self.check_nb_arguments(len(args)):
            raise CommandException("The number of arguments is not matching the command argument number needed.")

        return self.execution(args)

    @abstractmethod
    def check_args_type(self, args: [str]):
        """
        Check the arguments command.;
        :param args: The arguments to check.;
        :return: True if the arguments in parameter are valid; otherwise False.
        """
        pass

    @abstractmethod
    def execution(self, args: [str]):
        """
        Execution of the command.;
        :param args: The command arguments. ;
        """
        pass

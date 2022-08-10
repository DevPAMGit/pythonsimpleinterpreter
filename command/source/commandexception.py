class CommandException(Exception):
    """
    Custom exception for the command library.
    """

    def __init__(self, message: str):
        """
        Initialize a new instance of (CommandException)
        :param message:
        """
        super(CommandException, self).__init__()
        self.MESSAGE = message

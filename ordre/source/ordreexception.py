class OrdreException(Exception):
    """
    Classe personnalisée pour une exception lancée par un ordre donné à l'interpréteur.
    """

    def __init__(self, message: str):
        """
        Inialise une nouvelle instance de la classe 'OrdreException'.;
        :param message: Le message d'erreur de l'exception.
        """
        self.MESSAGE = message

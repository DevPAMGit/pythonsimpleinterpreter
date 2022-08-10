import re

from ordre.echoordre import EchoOrdre
from ordre.source.ordre import Ordre
from ordre.source.ordreexception import OrdreException


class Interpreteur:
    """
    Classe personnalisé représentant un interpreteur simple.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de la classe 'Interpreteur'.
        """
        self.COMMANDES: dict[str, Ordre] = {}
        self.ajt_ordre("echo", EchoOrdre())

    def ajt_ordre(self, nom: str, ordre: Ordre):
        """
        Méthode permettant d'ajouter un ordre dans l'interpréteur. ;
        :param nom: Le nom de l'ordre. ;
        :param ordre: L'ordre à exécuter. ;
        :raise OrdreException : Si le nom de la commande est vide ; Si le nom de la commande est déjà présent.
        """
        if ordre is None:
            return

        if nom is None or re.match("^\\s*$", nom) is not None:
            raise OrdreException("La commande à ajouter doit avoir un nom.")

        if nom in self.COMMANDES.keys():
            raise OrdreException("La commande '{0}' existe déjà.".format(nom))

        self.COMMANDES[nom] = ordre

    def interpreter(self, ordre: [str]):
        """
        Interprète un ordre passer à l'interpréteur.;
        :param ordre: L'ordre passé à l'interpréteur.;
        :raise OrdreException: Si l'exécution de l'ordre pose un problème.
        """
        ordre.pop(0)
        if len(ordre) == 0:
            raise OrdreException("Veuillez tapez une commande")

        if ordre[0] in self.COMMANDES.keys():
            self.COMMANDES[ordre.pop(0)].executer(ordre)
        else:
            raise OrdreException("La commande '" + ordre[0] + "' est inconnue.")

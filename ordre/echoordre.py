from abc import ABC

from ordre.source.ordre import Ordre
from ordre.source.ordreexception import OrdreException


class EchoOrdre(Ordre, ABC):
    """
    Ordre permettant d'afficher sur la sortie standard les éléments mis en paramètre.
    """

    def __init__(self):
        super().__init__(1)

    def __type_arguments__(self, args: [str]):
        """
        Sous méthode permettant de vérifier les arguments d'un appel d'ordres. ;
        :param args: La liste des arguments. ;
        :raise OrdreException: Si la vérification des arguments n'est pas probante.
        """
        if not isinstance(args[0], str):
            raise OrdreException("L'argument doit être une chaîne de caractères.")

    def __execution__(self, args: [str]):
        """
        Implémentation de l'exécution de la commande. ;
        :param args: La liste des arguments passés en paramètre. ;
        :raise OrdreException: Si une erreur intervient lors de l'exécution de la méthode.
        """
        print(args[0])
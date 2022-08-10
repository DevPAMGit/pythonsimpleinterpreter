from abc import ABC, abstractmethod

from ordre.source.ordreexception import OrdreException


class Ordre(ABC):
    """
    Classe personnalisé représentant un ordre à exécuter par l'interpréteur.
    """

    def __init__(self, nb_arguments: int):
        """
        Initialise une nouvelle instance de la classe 'Ordre'.;
        :param nb_arguments: Le nombre d'arguments attendu par l'ordre.
        """
        self.NB_ARGUMENTS = nb_arguments

    def executer(self, args: [str]):
        """
        Exécute l'ordre avec les arguments passé en paramètres. ;
        :param args: La liste des arguments passés en paramètres. ;
        :raise OrdreException: Si une erreur intervient lors de l'exécution de la méthode.
        """
        self.__preconditions__(args)
        self.__execution__(args)

    def __preconditions__(self, args: [str]):
        """
        Méthode permettant de vérifier les préconditions de l'ordre.;
        :param args: La liste des arguments.;
        :raise OrdreException: Si les arguments ne respectent pas les préconditions.
        """
        nb_arguments = len(args)
        if nb_arguments != self.NB_ARGUMENTS:
            raise OrdreException("La commande prend {0} argument{1}".format(str(nb_arguments),
                                                                            ("s" if nb_arguments > 0 else "")))
        self.__type_arguments__(args)

    @abstractmethod
    def __type_arguments__(self, args: [str]):
        """
        Sous méthode permettant de vérifier les arguments d'un appel d'ordres. ;
        :param args: La liste des arguments. ;
        :raise OrdreException: Si la vérification des arguments n'est pas probante.
        """
        pass

    @abstractmethod
    def __execution__(self, args: [str]):
        """
        Implémentation de l'exécution de la commande. ;
        :param args: La liste des arguments passés en paramètre. ;
        :raise OrdreException: Si une erreur intervient lors de l'exécution de la méthode.
        """
        pass

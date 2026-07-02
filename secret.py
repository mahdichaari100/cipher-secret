class Secret:
    """Classe pour chiffrer et déchiffrer des textes, listes, tuples et dictionnaires.

    Utilise la méthode du chiffrement de César avec un décalage personnalisable
    (négatif ou positif).
    """

    def __init__(self, decalage=1, numero=True):
        """Initialise la classe Secret avec un décalage et une règle pour les chiffres.

        numero : si True, les chiffres seront conservés.
                 si False, les chiffres seront chiffrés/déchiffrés.
        """
        if not isinstance(decalage, int):
            raise ValueError(
                f"Le décalage doit être de type int et pas {type(decalage).__name__}"
            )
        if not isinstance(numero, bool):
            raise ValueError("Le paramètre 'numero' doit être de type bool")

        self.__decalage = decalage
        self.__numero = numero
        self.__text_chiffre = ""
        self.__text_dechiffre = ""

        # Dictionnaires pour orienter le code selon le type de variable
        self.element_chiffrage = {
            "dict": self.dict_chiffre,
            "list": self.list_chiffre,
            "tuple": self.tuple_chiffre,
        }
        self.element_dechiffrage = {
            "dict": self.dict_dechiffre,
            "list": self.list_dechiffre,
            "tuple": self.tuple_dechiffre,
        }

    def chiffrage(self, element, dictionnaire="Values"):
        """Fonction principale pour chiffrer n'importe quel élément compatible.

        Pour le paramètre dictionnaire (si l'élément est un dictionnaire) :
        - "Values" : chiffre les valeurs seulement
        - "keys"   : chiffre les clés seulement
        - "both"   : chiffre les valeurs et les clés
        """
        if dictionnaire not in ["Values", "keys", "both"]:
            raise ValueError(
                f"Le paramètre dictionnaire='{dictionnaire}' doit être "
                f"inclus dans ['Values', 'keys', 'both']"
            )

        match element:
            case str():
                return self.chiffre(element)
            case list() | tuple():
                return self.element_chiffrage[type(element).__name__](element)
            case dict():
                return self.element_chiffrage["dict"](element, dictionnaire)
            case _:
                raise TypeError(
                    "L'élément à chiffrer doit être de type str, dict, list ou tuple"
                )

    def chiffre(self, chaine_chiffre):
        """Chiffre une chaîne de caractères (str)."""
        self.__text_chiffre = ""
        for i in chaine_chiffre:
            if i.isalpha():
                if "a" <= i <= "z":
                    self.__text_chiffre += chr(
                        (ord(i) - ord("a") + self.__decalage) % 26 + ord("a")
                    )
                elif "A" <= i <= "Z":
                    self.__text_chiffre += chr(
                        (ord(i) - ord("A") + self.__decalage) % 26 + ord("A")
                    )
            elif not self.__numero and i.isdigit():
                # Chiffrement des chiffres de 0 à 9 si numero=False
                self.__text_chiffre += chr(
                    (ord(i) - ord("0") + self.__decalage) % 10 + ord("0")
                )
            else:
                self.__text_chiffre += i
        return self.__text_chiffre

    def list_chiffre(self, element):
        """Chiffre tous les textes d'un tableau (list)."""
        liste_a_chiffrer = list(element)
        return list(map(self.chiffre, liste_a_chiffrer))

    def tuple_chiffre(self, element):
        """Chiffre tous les textes d'un tuple."""
        tuple_a_chiffrer = list(element)
        return tuple(map(self.chiffre, tuple_a_chiffrer))

    def dict_chiffre(self, element, a_chiffrer):
        """Chiffre un dictionnaire (clés, valeurs ou les deux)."""
        dictionnaire_a_chiffrer = {}
        match a_chiffrer:
            case "Values":
                for keys, value in element.items():
                    dictionnaire_a_chiffrer[keys] = self.chiffre(value)
            case "keys":
                for keys, value in element.items():
                    dictionnaire_a_chiffrer[self.chiffre(keys)] = value
            case "both":
                for keys, value in element.items():
                    dictionnaire_a_chiffrer[self.chiffre(keys)] = self.chiffre(
                        value
                    )
        return dictionnaire_a_chiffrer

    # --- PARTIE DÉCHIFFRAGE ---

    def dechiffrage(self, element, dictionnaire="Values"):
        """Fonction principale pour déchiffrer n'importe quel élément compatible.

        Pour le paramètre dictionnaire (si l'élément est un dictionnaire) :
        - "Values" : déchiffre les valeurs seulement
        - "keys"   : déchiffre les clés seulement
        - "both"   : déchiffre les valeurs et les clés
        """
        if dictionnaire not in ["Values", "keys", "both"]:
            raise ValueError(
                f"Le paramètre dictionnaire='{dictionnaire}' doit être "
                f"inclus dans ['Values', 'keys', 'both']"
            )

        match element:
            case str():
                return self.dechiffre(element)
            case list() | tuple():
                return self.element_dechiffrage[type(element).__name__](element)
            case dict():
                return self.element_dechiffrage["dict"](element, dictionnaire)
            case _:
                raise TypeError(
                    "L'élément à déchiffrer doit être de type str, dict, list ou tuple"
                )

    def dechiffre(self, chaine_dechiffre):
        """Déchiffre une chaîne de caractères (str)."""
        self.__text_dechiffre = ""
        for i in chaine_dechiffre:
            if i.isalpha():
                if "a" <= i <= "z":
                    self.__text_dechiffre += chr(
                        (ord(i) - ord("a") - self.__decalage) % 26 + ord("a")
                    )
                elif "A" <= i <= "Z":
                    self.__text_dechiffre += chr(
                        (ord(i) - ord("A") - self.__decalage) % 26 + ord("A")
                    )
            elif not self.__numero and i.isdigit():
                self.__text_dechiffre += chr(
                    (ord(i) - ord("0") - self.__decalage) % 10 + ord("0")
                )
            else:
                self.__text_dechiffre += i
        return self.__text_dechiffre

    def list_dechiffre(self, element):
        """Déchiffre tous les textes d'un tableau (list)."""
        liste_a_déchiffrer = list(element)
        return list(map(self.dechiffre, liste_a_déchiffrer))

    def tuple_dechiffre(self, element):
        """Déchiffre tous les textes d'un tuple."""
        tuple_a_déchiffrer = list(element)
        return tuple(map(self.dechiffre, tuple_a_déchiffrer))

    def dict_dechiffre(self, element, a_dechiffrer):
        """Déchiffre un dictionnaire (clés, valeurs ou les deux)."""
        dictionnaire_a_dechiffrer = {}
        match a_dechiffrer:
            case "Values":
                for keys, value in element.items():
                    dictionnaire_a_dechiffrer[keys] = self.dechiffre(value)
            case "keys":
                for keys, value in element.items():
                    dictionnaire_a_dechiffrer[self.dechiffre(keys)] = value
            case "both":
                for keys, value in element.items():
                    dictionnaire_a_dechiffrer[self.dechiffre(keys)] = (
                        self.dechiffre(value)
                    )
        return dictionnaire_a_dechiffrer



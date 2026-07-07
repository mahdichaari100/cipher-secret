# Méthode de chiffrement "Cesar"

class Cesar:
    """Logique pure du chiffrement de César par décalage fixe."""

    def __init__(self, decalage=1, numero=True):
        """Initialise la classe Cesar avec un décalage et une règle pour les chiffres.

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

    def list_dechiffre(self, element):
        """Déchiffre tous les textes d'un tableau (list)."""
        liste_a_dechiffrer = list(element)
        return list(map(self.dechiffre, liste_a_dechiffrer))

    def tuple_dechiffre(self, element):
        """Déchiffre tous les textes d'un tuple."""
        tuple_a_dechiffrer = list(element)
        return tuple(map(self.dechiffre, tuple_a_dechiffrer))

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

    def chiffre(self, chaine):
        """Chiffre une chaîne de caractères, un int ou un float par décalage."""
        chaine_chiffre = str(chaine)
        self.__text_chiffre = ""
        for i in chaine_chiffre:
            if i.isalpha():
                if "a" <= i <= "z":
                    # Modulo 26 pour faire boucler l'alphabet minuscule en continu
                    self.__text_chiffre += chr(
                        (ord(i) - ord("a") + self.__decalage) % 26 + ord("a")
                    )
                elif "A" <= i <= "Z":
                    # Modulo 26 pour faire boucler l'alphabet majuscule en continu
                    self.__text_chiffre += chr(
                        (ord(i) - ord("A") + self.__decalage) % 26 + ord("A")
                    )
            elif not self.__numero and i.isdigit():
                # Modulo 10 pour faire boucler la suite des chiffres de 0 à 9
                self.__text_chiffre += chr(
                    (ord(i) - ord("0") + self.__decalage) % 10 + ord("0")
                )
            else:
                self.__text_chiffre += i

        if isinstance(chaine, int):
            return int(self.__text_chiffre)
        elif isinstance(chaine, float):
            return float(self.__text_chiffre)
        return self.__text_chiffre

    def dechiffre(self, chaine):
        """Déchiffre une chaîne de caractères, un int ou un float par décalage."""
        chaine_dechiffre = str(chaine)
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

        if isinstance(chaine, int):
            return int(self.__text_dechiffre)
        elif isinstance(chaine, float):
            return float(self.__text_dechiffre)
        return self.__text_dechiffre


# méthode de chiffrement "Vigenere"
    
class Vigenere:
    """Logique pure du chiffrement de Vigenère par clé textuelle."""

    def __init__(self, cle="SECRET", numero=True):
        """Initialise la classe Vigenere avec une clé et une règle pour les chiffres.

        numero : si True, les chiffres seront conservés.
                 si False, les chiffres seront chiffrés/déchiffrés.
        """
        if not isinstance(cle, str):
            raise ValueError(
                f"La clé doit être de type str et pas {type(cle).__name__}"
            )
        if not isinstance(numero, bool):
            raise ValueError("Le paramètre 'numero' doit être de type bool")

        self.__cle = cle
        self.__numero = numero
        self.__text_chiffre = ""
        self.__text_dechiffre = ""
        self.__list_decalage = []

        # Transformer la clé en liste de décalages numériques (A=0; B=1; C=2; ...; Z=25)
        cle_majuscule = cle.upper()
        for i in cle_majuscule:
            self.__list_decalage.append(ord(i) - 65)

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

    def list_dechiffre(self, element):
        """Déchiffre tous les textes d'un tableau (list)."""
        liste_a_dechiffrer = list(element)
        return list(map(self.dechiffre, liste_a_dechiffrer))

    def tuple_dechiffre(self, element):
        """Déchiffre tous les textes d'un tuple."""
        tuple_a_dechiffrer = list(element)
        return tuple(map(self.dechiffre, tuple_a_dechiffrer))

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

    def chiffre(self, chaine):
        """Chiffre une chaîne de caractères (str), un int ou un float."""
        chaine_chiffre = str(chaine)
        self.__text_chiffre = ""
        index_cle = 0  # Permet d'avancer dans la clé uniquement pour les lettres lues

        for i in range(len(chaine_chiffre)):
            # Sélection du décalage correspondant à la lettre actuelle de la clé
            decalage = self.__list_decalage[index_cle % len(self.__list_decalage)]

            if chaine_chiffre[i].isalpha():
                if "a" <= chaine_chiffre[i] <= "z":
                    self.__text_chiffre += chr(
                        (ord(chaine_chiffre[i]) - ord("a") + decalage) % 26 + ord("a")
                    )
                elif "A" <= chaine_chiffre[i] <= "Z":
                    self.__text_chiffre += chr(
                        (ord(chaine_chiffre[i]) - ord("A") + decalage) % 26 + ord("A")
                    )
                index_cle += 1  # La clé avance car on a chiffré une lettre
            elif not self.__numero and chaine_chiffre[i].isdigit():
                # Chiffrement des chiffres de 0 à 9 si numero=False
                self.__text_chiffre += chr(
                    (ord(chaine_chiffre[i]) - ord("0") + decalage) % 10 + ord("0")
                )
                index_cle += 1  # La clé avance car on a chiffré un chiffre
            else:
                # Les espaces et symboles sont recopiés sans faire avancer la clé
                self.__text_chiffre += chaine_chiffre[i]

        if isinstance(chaine, int):
            return int(self.__text_chiffre)
        elif isinstance(chaine, float):
            return float(self.__text_chiffre)
        return self.__text_chiffre

    def dechiffre(self, chaine):
        """Déchiffre une chaîne de caractères (str), un int ou un float."""
        chaine_dechiffre = str(chaine)
        self.__text_dechiffre = ""
        index_cle = 0  # Permet de reculer dans la clé uniquement pour les lettres lues

        for i in range(len(chaine_dechiffre)):
            decalage = self.__list_decalage[index_cle % len(self.__list_decalage)]

            if chaine_dechiffre[i].isalpha():
                if "a" <= chaine_dechiffre[i] <= "z":
                    self.__text_dechiffre += chr(
                        (ord(chaine_dechiffre[i]) - ord("a") - decalage) % 26 + ord("a")
                    )
                elif "A" <= chaine_dechiffre[i] <= "Z":
                    self.__text_dechiffre += chr(
                        (ord(chaine_dechiffre[i]) - ord("A") - decalage) % 26 + ord("A")
                    )
                index_cle += 1
            elif not self.__numero and chaine_dechiffre[i].isdigit():
                self.__text_dechiffre += chr(
                    (ord(chaine_dechiffre[i]) - ord("0") - decalage) % 10 + ord("0")
                )
                index_cle += 1
            else:
                self.__text_dechiffre += chaine_dechiffre[i]

        if isinstance(chaine, int):
            return int(self.__text_dechiffre)
        elif isinstance(chaine, float):
            return float(self.__text_dechiffre)
        return self.__text_dechiffre




class Secret:
    """Classe pour chiffrer et déchiffrer des textes, listes, tuples et dictionnaires.

    Selon deux méthodes ("cesar" ou "vigenere").
    """

    def __init__(self, methode="cesar", **kwargs):
        # Validation stricte des arguments bonus autorisés
        
        if not all(x in ["decalage", "numero", "cle"] for x in list(kwargs.keys())):
            raise ValueError(
                "Les arguments choisis autre que methode sont "
                "(decalage=nombre ou numero=True or False, cle=string)"
            )

        if methode == "cesar":
            self.moteur = Cesar(
                decalage=kwargs.get("decalage", 1),
                numero=kwargs.get("numero", True)
            )
        elif methode == "vigenere":
            self.moteur = Vigenere(
                cle=kwargs.get("cle", "SECRET"),
                numero=kwargs.get("numero", True)
            )
        else:
            raise ValueError("Méthode inconnue. Choisissez 'cesar' ou 'vigenere'.")

    # --- PARTIE CHIFFRAGE ---

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
                return self.moteur.chiffre(element)
            case list() | tuple():
                return self.moteur.element_chiffrage[type(element).__name__](element)
            case dict():
                return self.moteur.element_chiffrage["dict"](element, dictionnaire)
            case _:
                raise TypeError(
                    "L'élément à chiffrer doit être de type str, dict, list ou tuple"
                )

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

        # Appeler la classe selon la méthode choisie et quelques données
        
        match element:
            case str():
                return self.moteur.dechiffre(element)
            case list() | tuple():
                return self.moteur.element_dechiffrage[type(element).__name__](element)
            case dict():
                return self.moteur.element_dechiffrage["dict"](element, dictionnaire)
            case _:
                raise TypeError(
                    "L'élément à déchiffrer doit être de type str, dict, list ou tuple"
                )


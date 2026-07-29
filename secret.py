import string
import sys
import unicodedata
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
        chaine_chiffre = enlever_accents( str(chaine) )
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
        chaine_chiffre = enlever_accents( str(chaine) )
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

def enlever_accents(texte):
    # Décompose les caractères accentués
    normalise = unicodedata.normalize('NFD', texte)
    # Filtre pour garder uniquement les caractères qui ne sont pas des diacritiques
    sans_accents = ''.join(c for c in normalise if unicodedata.category(c) != 'Mn')
    return sans_accents


"""
    Partie déchiffrer les textes chiffré en anglais seulement
    ce code peut déchiffrer les texte contenant plusque 150 caractères
    attention: ce code peut faire des erreurs si le texte est court et la clé contient plusque 6 caractère
"""
# Les fréquences d'apparition des lettres en anglais (de A à Z)
ENGLISH_FREQS = [
    0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697,
    0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599,
    0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
]

def nettoyer_texte(texte):
    """Garde uniquement les lettres en majuscules pour faciliter les calculs."""
    return "".join([c.upper() for c in texte if c.isalpha()])

def indice_coincidence(texte):
    """Calcule l'Indice de Coïncidence (IC) pour mesurer la répétition des lettres."""
    n = len(texte)
    if n <= 1:
        return 0.0
    frequences = [texte.count(lettre) for lettre in string.ascii_uppercase]
    somme = sum(f * (f - 1) for f in frequences)
    return somme / (n * (n - 1))

def deviner_taille_cle(texte_nettoye, taille_max=20):
    """Trouve la longueur de clé la plus petite et probable en utilisant un seuil d'IC."""
    for taille in range(1, taille_max + 1):
        ics = []
        for i in range(taille):
            sous_groupe = texte_nettoye[i::taille]
            ics.append(indice_coincidence(sous_groupe))
        
        ic_moyen = sum(ics) / len(ics)
        
        # Correction : Si l'IC dépasse 0.060, on valide immédiatement la taille.
        # Cela empêche le programme de choisir un multiple comme 12 au lieu de 6.
        if ic_moyen > 0.060:
            return taille
            
    return 1

def deviner_lettre_cle(sous_groupe):
    """Trouve la meilleure lettre de décalage en comparant avec l'anglais. en utilisant la règle de "Khi-deux" """
    n = len(sous_groupe)
    meilleur_score = float('inf')
    meilleur_decalage = 0
    
    for decalage in range(26): #tester tout les décalage possibe 
        frequences_observees = [0] * 26
        for lettre in sous_groupe:
            index = (ord(lettre) - ord('A') - decalage) % 26
            frequences_observees[index] += 1
            
        score = 0
        for i in range(26):
            attendue = n * ENGLISH_FREQS[i]
            observee = frequences_observees[i]
            if attendue > 0:
                score += ((observee - attendue) ** 2) / attendue
                
        if score < meilleur_score:
            meilleur_score = score
            meilleur_decalage = decalage
            
    return chr(ord('A') + meilleur_decalage)

def casser_vigenere(texte_code):
    """Fonction principale pour trouver la clé et déchiffrer le message."""
    texte_nettoye = nettoyer_texte(texte_code)
    if len(texte_nettoye)<150 :
        sys.exit("Erreur : il faut que le texte contient plus que 150 lettres !")
    # 1. Trouver la taille de la clé
    taille_cle = deviner_taille_cle(texte_nettoye)
    print(f"[+] Longueur de clé détectée : {taille_cle} lettres")
    
    # 2. Trouver chaque lettre de la clé
    cle = ""
    for i in range(taille_cle):
        sous_groupe = texte_nettoye[i::taille_cle]
        cle += deviner_lettre_cle(sous_groupe)
    print(f"[+] Clé secrète découverte : {cle}")
    
    # 3. Déchiffrer le texte d'origine avec la clé trouvée
    texte_dechiffre = []
    index_cle = 0
    for caractere in texte_code:
        if caractere.isalpha():
            est_majuscule = caractere.isupper()
            decalage = ord(cle[index_cle % taille_cle]) - ord('A')
            
            origine = ord(caractere.upper()) - decalage
            if origine < ord('A'):
                origine += 26
                
            lettre_finale = chr(origine)
            texte_dechiffre.append(lettre_finale if est_majuscule else lettre_finale.lower())
            index_cle += 1
        else:
            texte_dechiffre.append(caractere)
            
    return "".join(texte_dechiffre)

# --- ZONE DE TEST ---

def afficher(message_secret):
    print("-----ce code peut faire des erreur avec les textes courts et les clés longues-----")
    print("--- Lancement de la cyber-analyse ---")
    resultat = casser_vigenere(message_secret)
    print("\n[+] Message déchiffré :\n")
    print(resultat)

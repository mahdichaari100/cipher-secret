# cipher-secret-mahdi

Une librairie Python moderne, robuste et conforme à la norme PEP 8 pour chiffrer et déchiffrer des données en utilisant deux méthodes célèbres : **César** (décalage fixe) et **Vigenère** (mot-clé répétitif).

Cette boîte à outils traite intelligemment les chaînes de caractères, les nombres (`int`, `float`), ainsi que les structures complexes (`list`, `tuple`, `dict`).

---

## 🚀 Installation

Ouvrez votre terminal ou invite de commandes (**cmd**) et tapez :
```bash
pip install cipher-secret-mahdi
```

---

## 🛠️ Guide complet des fonctionnalités (Tous les cas possibles)

Pour commencer, importez toujours la classe principale `Secret` :
```python
from secret import Secret
```

### Cas 1 : Chiffrement de César (Textes et Nombres)
Le chiffrement de César décale les lettres d'un nombre fixe de positions. Vos fonctions préservent automatiquement le type d'origine (`int` ou `float`).

```python
# Initialisation avec un décalage de 3 positions
# numero=True : les chiffres (0-9) restent inchangés
outil_cesar = Secret(methode="cesar", decalage=3, numero=True)

# --- Chaîne de caractères (str) ---
texte_chiffre = outil_cesar.chiffrage("Bonjour")
print(texte_chiffre)  # Affiche : Erqmrxu
print(outil_cesar.dechiffrage(texte_chiffre))  # Affiche : Bonjour

# --- Nombre Entier (int) avec numero=False ---
# Pour chiffrer des nombres, il faut obligatoirement configurer numero=False
outil_cesar_num = Secret(methode="cesar", decalage=1, numero=False)
entier_chiffre = outil_cesar_num.chiffrage(123)
print(entier_chiffre)  # Affiche l'entier : 234 (Le type int est conservé !)
print(outil_cesar_num.dechiffrage(entier_chiffre))  # Affiche : 123

# --- Nombre Flottant (float) avec numero=False ---
float_chiffre = outil_cesar_num.chiffrage(12.3)
print(float_chiffre)  # Affiche le float : 23.4 (Le type float est conservé !)
print(outil_cesar_num.dechiffrage(float_chiffre))  # Affiche : 12.3
```

### Cas 2 : Chiffrement de Vigenère (Listes et Tuples)
Le chiffrement de Vigenère utilise un mot-clé. L'index de la clé avance de manière fluide uniquement lorsqu'une lettre (ou un chiffre modifié) est rencontrée.

```python
# Initialisation avec la clé "CHAT"
outil_vigenere = Secret(methode="vigenere", cle="CHAT", numero=True)

# --- Tableaux / Listes (list) ---
ma_liste = ["Code", "Secret"]
liste_codee = outil_vigenere.chiffrage(ma_liste)
print(liste_codee)  # Affiche la liste chiffrée
print(outil_vigenere.dechiffrage(liste_codee))  # Recommence et affiche : ['Code', 'Secret']

# --- Tuples (tuple) ---
mon_tuple = ("Python", "Mahdi")
tuple_code = outil_vigenere.chiffrage(mon_tuple)
print(tuple_code)  # Affiche le tuple chiffré (Le type tuple est conservé !)
print(outil_vigenere.dechiffrage(tuple_code))  # Affiche : ('Python', 'Mahdi')
```

### Cas 3 : Les 3 configurations pour les Dictionnaires (`dict`)
Le paramètre optionnel `dictionnaire` offre trois stratégies distinctes pour cibler précisément ce que vous souhaitez masquer dans vos dictionnaires.

```python
outil = Secret(methode="cesar", decalage=3)
donnees = {"nom": "Alice", "ville": "Tunis"}

# --- Option A : "Values" (Par défaut) ---
# Seules les valeurs du dictionnaire sont modifiées, les clés restent lisibles.
dict_values = outil.chiffrage(donnees, dictionnaire="Values")
print(dict_values)  # Affiche : {'nom': 'Dolfh', 'ville': 'Wxqiv'}
print(outil.dechiffrage(dict_values, dictionnaire="Values"))

# --- Option B : "keys" ---
# Seules les clés du dictionnaire sont masquées, les valeurs restent intactes.
dict_keys = outil.chiffrage(donnees, dictionnaire="keys")
print(dict_keys)  # Affiche : {'qrp': 'Alice', ' ylooh': 'Tunis'}
print(outil.dechiffrage(dict_keys, dictionnaire="keys"))

# --- Option C : "both" ---
# Chiffre intégralement le dictionnaire (Clés ET Valeurs).
dict_both = outil.chiffrage(donnees, dictionnaire="both")
print(dict_both)  # Affiche : {'qrp': 'Dolfh', ' ylooh': 'Wxqiv'}
print(outil.dechiffrage(dict_both, dictionnaire="both"))
```

---

## ⚠️ Gestion des erreurs et sécurité
La librairie intègre des vérifications strictes pour vous aider à coder sans commettre d'erreurs :

*   **`ValueError`** : Déclenchée si vous tentez de passer un argument inconnu à la classe `Secret` (comme un décalage qui ne serait pas un entier, une clé qui ne serait pas un texte, ou un paramètre bonus non répertorié).
*   **`TypeError`** : Déclenchée si vous essayez de chiffrer un type de données non supporté (comme un booléen ou un ensemble `set`).

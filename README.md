# cipher-secret

Une librairie Python moderne pour chiffrer et déchiffrer des textes, listes et dictionnaires avec le chiffrement de César.

## 🛠️ Exemple d'utilisation

Voici comment utiliser la classe `Secret` dans votre code Python :

```python
from secret import Secret

# 1. Initialisation avec un décalage de 3 positions
# numero=True : les chiffres (0-9) ne sont pas modifiés
outil = Secret(decalage=3, numero=True)

# --- CHIFFREMENT ---
# Chiffrer un texte simple
texte_cache = outil.chiffrage("Bonjour tout le monde ! 2026")
print(texte_cache)  # Affiche : Erqmrxu wrxw oh prqgh ! 2026

# Chiffrer une liste
liste_cachee = outil.chiffrage(["Code", "Secret"])
print(liste_cachee)  # Affiche : ['Frgh', 'Vhfuhw']

# Chiffrer les valeurs d'un dictionnaire
mon_dict = {"pseudo": "Alice", "statut": "Admin"}
dict_cache = outil.chiffrage(mon_dict, dictionnaire="Values")
print(dict_cache)  # Affiche : {'pseudo': 'Dolfh', 'statut': 'Adplq'}


# --- DÉCHIFFREMENT ---
# Déchiffrer le texte
texte_original = outil.dechiffrage(texte_cache)
print(texte_original)  # Affiche : Bonjour tout le monde ! 2026
```


import re
from pathlib import Path
import shutil

source = Path("/Users/morganr/Desktop/Flaubert, Gustave/textes_extraits_Flaubert/Trois contes.txt")
destination = source.with_name(source.stem + "_travail.txt")

def nettoyage_structure_epub(texte):
    #1. Supprimer le titre du livre (en majuscules) 
    texte = re.sub(r"", "", texte, flags=re.IGNORECASE) #on ajoute ici le titre du livre 
    
    #2. Supprimer les listes et tables des matières
    pattern_tables = r"Liste des titres|Table des matières du titre|Table des matières"
    texte = re.sub(pattern_tables, "", texte, flags=re.IGNORECASE)
    
    #3. Supprimer les numéros de chapitres
    #pattern_chapitres = r"Chapitre [IVXLCDM\d]+" #pour supprimer les chapitres avec le mot "Chapitre" devant
    #pattern_chapitres_alt = r"\b[IVXLCDM]+\b(?![’'])|\b\d+\b" #pour supprimer les chapitres qui sont juste des numéros romains ou arabes isolés (sans le mot "Chapitre" devant)
    #pattern_chapitre_complexe = r"^\s*[IVXLCDM]+\b(?![’'])\s*[–—\-\.:]?\s+.*",# pour supprimer les chapitres qui sont des numéros romains suivis d'un titre 
    texte = re.sub(, "", texte, flags=re.MULTILINE | re.IGNORECASE ) #ici on choisi le parterne que l'on veut supprimer
    
    #4. Supprimer les annotations entre crochets 
    texte = re.sub(r'\[.*?\]', '', texte)
    
    #5. supprimer les "FIN DE"
    texte = re.sub(r"^\s*FIN\s+DE.*", '', texte, flags=re.M | re.I)
    
    #6. Nettoyage des lignes vides multiples (remplacées par un seul saut de ligne)
    texte = re.sub(r'\n\s*\n', '\n', texte)
    
    
    return texte.strip()

try:
    # 1. Lecture du fichier brut
    with open(source, "r", encoding="utf-8") as f:
        contenu_brut = f.read()

    # 2. Application du nettoyage
    contenu_propre = nettoyage_structure_epub(contenu_brut)

    # 3. Sauvegarde du nouveau fichier
    with open(destination, "w", encoding="utf-8") as f:
        f.write(contenu_propre)

    print(f"Nettoyage terminé ! Le fichier propre est ici : {destination}")

except FileNotFoundError:
    print(" Erreur : Le fichier source est introuvable. Vérifie le chemin et l'extension (.txt).")
# Cleaning_Romans_Flaubert
Scprit Regex pour nottoyer un texte en ".txt" et le sortir en nouveau fichier


#  Flaubert Text Cleaner

Ce script Python permet de nettoyer et de normaliser des fichiers textes (issus de conversions d'e-books ou d'OCR) en supprimant les scories structurelles (tables des matières, numéros de chapitres, annotations). 

Il a été initialement conçu pour traiter les œuvres de **Gustave Flaubert** (notamment *Trois Contes*), mais peut être adapté à n'importe quel projet de nettoyage de texte littéraire.

##  Fonctionnalités

Le script applique une série de transformations via des expressions régulières (Regex) :
* **Nettoyage structurel :** Suppression des titres de livres et des mentions "FIN DE".
* **Tables des matières :** Élimination automatique des listes de titres et sommaires.
* **Numérotation :** Suppression flexible des numéros de chapitres (chiffres romains ou arabes).
* **Annotations :** Retrait de toutes les notes ou métadonnées entre crochets `[...]`.
* **Normalisation :** Réduction des sauts de lignes multiples pour un texte compact et propre.

## Installation

Aucune bibliothèque externe n'est requise ! Le script utilise uniquement la bibliothèque standard de Python.

1.  Assurez-vous d'avoir **Python 3.x** installé.
2.  Clonez ce dépôt ou téléchargez le fichier `nettoyage_textes_Flaubert.py`.
3.  Placez votre fichier `.txt` source dans le dossier de votre choix.

## Configuration & Usage

Avant de lancer le script, vous devez configurer les chemins de fichiers dans le code :

1.  Ouvrez le script et modifiez la variable `source` :
    ```python
    source = Path("/votre/chemin/vers/le/fichier.txt")
    ```
2.  Lancez le script :
    ```bash
    python nettoyage_textes_Flaubert.py
    ```

Le script générera automatiquement un nouveau fichier suffixé par `_travail.txt` dans le même répertoire.

##  Personnalisation

Le script est conçu pour être modulaire. Dans la fonction `nettoyage_structure_epub`, vous pouvez décommenter ou modifier les patterns Regex selon vos besoins :
* **Chapitres :** Vous pouvez choisir de supprimer uniquement le mot "Chapitre" ou les numéros isolés.
* **Titres spécifiques :** Une zone est prévue pour ajouter manuellement le titre de l'œuvre à supprimer.

## Prérequis

* **Python 3.6+**
* Un fichier texte encodé en **UTF-8**.


import os
import re
from datetime import datetime

# Fonction pour convertir la date
def convert_date(date_string):
    try:
        # Enlever le suffixe 'th', 'st', 'nd', 'rd' du jour
        date_string = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_string)
        date_object = datetime.strptime(date_string, "%B %d, %Y %I:%M%p")
        return date_object.isoformat()
    except ValueError:
        return date_string  # Retourne la chaîne d'origine si le format ne correspond pas

# Chemin du répertoire contenant les fichiers Markdown
directory_path = 'content/articles/'  # Remplacez par le chemin de votre dossier

# Parcourir tous les fichiers dans le répertoire
for filename in os.listdir(directory_path):
    if filename.endswith('.html'):  # Vérifie si le fichier est un fichier Markdown
        file_path = os.path.join(directory_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Trouver et remplacer toutes les occurrences de la date
        new_content = re.sub(r'(\w+ \d+(st|nd|rd|th), \d+ \d{1,2}:\d{2}(am|pm))', lambda x: convert_date(x.group(0)), content)

        # Écrire le nouveau contenu dans le fichier
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Conversion terminée.")

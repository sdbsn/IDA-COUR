import os
import json
import webbrowser
from urllib.parse import urlparse, parse_qs

def get_file_ids():
    """Obtenir les IDs des fichiers Google Drive"""
    file_ids = {}
    
    # Dossiers à traiter
    folders = ['ASSETS', 'files']
    
    for folder in folders:
        if os.path.exists(folder):
            for root, _, files in os.walk(folder):
                for file in files:
                    filepath = os.path.join(root, file)
                    file_ids[filepath] = ""
    
    return file_ids

def open_google_drive():
    """Ouvrir Google Drive dans le navigateur"""
    webbrowser.open('https://drive.google.com')

def get_drive_id(url):
    """Extraire l'ID Google Drive d'une URL"""
    try:
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        return query_params.get('id', [''])[0]
    except:
        return ""

def main():
    # Obtenir la liste des fichiers
    file_ids = get_file_ids()
    
    # Ouvrir Google Drive
    print("Ouverture de Google Drive...")
    open_google_drive()
    
    print("\nInstructions:")
    print("1. Téléchargez vos fichiers dans Google Drive")
    print("2. Pour chaque fichier, cliquez avec le bouton droit")
    print("3. Sélectionnez 'Partager'")
    print("4. Copiez l'URL partagée")
    
    # Créer le fichier de configuration
    config = {
        "videos": {
            "base": "https://drive.google.com/uc?export=view&id=",
            "ids": {}
        },
        "assets": {
            "base": "https://drive.google.com/uc?export=view&id=",
            "ids": {}
        }
    }
    
    # Sauvegarder la configuration initiale
    with open('drive-config.json', 'w') as f:
        json.dump(config, f, indent=4)
    
    print("\nConfiguration initiale sauvegardée dans drive-config.json")
    print("Vous pouvez maintenant mettre à jour les IDs avec les vrais IDs Google Drive")

if __name__ == "__main__":
    main()

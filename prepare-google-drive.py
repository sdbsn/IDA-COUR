import os
import json

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
                    # Ici vous devrez remplir les IDs manuellement
                    # Pour chaque fichier, obtenez l'ID Google Drive et ajoutez-le
                    file_ids[filepath] = "YOUR_GOOGLE_DRIVE_ID"
    
    return file_ids

def update_config(file_ids):
    """Mettre à jour le fichier de configuration"""
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
    
    # Séparer les vidéos et les autres assets
    for filepath, file_id in file_ids.items():
        if filepath.endswith(('.mp4', '.avi', '.mov')):
            config["videos"]["ids"][os.path.basename(filepath)] = file_id
        else:
            config["assets"]["ids"][os.path.basename(filepath)] = file_id
    
    return config

def main():
    # Obtenir les IDs des fichiers
    file_ids = get_file_ids()
    
    # Mettre à jour le fichier de configuration
    config = update_config(file_ids)
    
    # Sauvegarder le fichier de configuration
    with open('drive-config.json', 'w') as f:
        json.dump(config, f, indent=4)
    
    print("Configuration sauvegardée dans drive-config.json")
    print("Vous devez maintenant remplir les IDs Google Drive pour chaque fichier")

if __name__ == "__main__":
    main()

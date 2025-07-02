// Configuration des liens Google Drive
const driveLinks = {
    videos: {
        base: "https://drive.google.com/uc?export=view&id=",
        ids: {
            // Ajoutez ici les IDs de vos fichiers Google Drive
            // Exemple: "video1": "123456789"
        }
    },
    assets: {
        base: "https://drive.google.com/uc?export=view&id=",
        ids: {
            // Ajoutez ici les IDs de vos fichiers Google Drive
        }
    }
};

// Fonction pour générer les URLs
function getDriveUrl(type, key) {
    return driveLinks[type].base + driveLinks[type].ids[key];
}

export { driveLinks, getDriveUrl };

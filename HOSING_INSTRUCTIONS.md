# Instructions d'Hébergement Google Drive

## 1. Préparation des fichiers

1. Créez un compte Google Drive si vous n'en avez pas déjà un
2. Créez un nouveau dossier Google Drive nommé "IDA-COUR"
3. Partagez ce dossier en lecture seule
4. Téléchargez-y vos fichiers volumineux (vidéos, images, PDFs)

## 2. Obtenir les IDs Google Drive

Pour chaque fichier :
1. Cliquez avec le bouton droit sur le fichier
2. Sélectionnez "Partager"
3. Copiez l'ID du fichier (c'est la partie après "id=" dans l'URL)

## 3. Mettre à jour la configuration

1. Ouvrez le fichier `drive-config.json`
2. Remplacez "YOUR_GOOGLE_DRIVE_ID" par les vrais IDs
3. Organisez les fichiers dans les catégories appropriées :
   - vidéos
   - assets

## 4. Déploiement sur Netlify

1. Allez sur [Netlify](https://app.netlify.com)
2. Connectez votre compte GitHub
3. Sélectionnez votre dépôt
4. Configurez les paramètres de déploiement :
   - Build command: `echo "Build complete"`
   - Publish directory: `./`

## 5. Vérification

1. Vérifiez que tous les liens fonctionnent
2. Testez le chargement des ressources
3. Assurez-vous que les images et vidéos s'affichent correctement

## 6. Maintenance

1. Ajoutez les nouveaux fichiers dans Google Drive
2. Mettez à jour la configuration avec les nouveaux IDs
3. Déployez les changements sur Netlify

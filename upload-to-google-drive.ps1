# Script PowerShell pour aider à l'upload sur Google Drive

# Fonction pour obtenir l'ID Google Drive d'une URL
function Get-GoogleDriveId {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Url
    )
    
    $uri = [System.Uri]$Url
    $query = [System.Web.HttpUtility]::ParseQueryString($uri.Query)
    return $query['id']
}

# Liste des fichiers à télécharger
$filesToUpload = @(
    # Images
    "ASSETS\html.png",
    "ASSETS\css.png",
    "ASSETS\js.png",
    "ASSETS\php.png",
    "ASSETS\python.jpeg",
    "ASSETS\vue js.jpeg",
    "ASSETS\angular.png",
    "ASSETS\uvs.png",
    "ASSETS\téléchargement (2).jpg",
    "files\ChatGPT Image 1 juil. 2025, 03_24_36.png"
)

# Afficher les instructions
Write-Host "`nInstructions pour l'upload sur Google Drive:`n" -ForegroundColor Cyan
Write-Host "1. Créez un dossier Google Drive nommé 'IDA-COUR'" -ForegroundColor Green
Write-Host "2. Partagez le dossier en lecture seule" -ForegroundColor Green
Write-Host "3. Pour chaque fichier :" -ForegroundColor Green
Write-Host "   - Cliquez avec le bouton droit sur le fichier" -ForegroundColor Green
Write-Host "   - Sélectionnez 'Partager'" -ForegroundColor Green
Write-Host "   - Copiez l'URL partagée" -ForegroundColor Green
Write-Host "   - Notez l'ID dans le fichier drive-config.json" -ForegroundColor Green

# Ouvrir Google Drive
Write-Host "`nOuverture de Google Drive..." -ForegroundColor Yellow
Start-Process "https://drive.google.com"

# Attendre que l'utilisateur soit prêt
Read-Host "Appuyez sur Entrée une fois que vous avez créé et partagé le dossier Google Drive"

# Afficher la liste des fichiers à télécharger
Write-Host "`nListe des fichiers à télécharger :" -ForegroundColor Cyan
foreach ($file in $filesToUpload) {
    if (Test-Path $file) {
        Write-Host "✓ $file" -ForegroundColor Green
    } else {
        Write-Host "✗ $file (fichier non trouvé)" -ForegroundColor Red
    }
}

# Attendre que l'utilisateur termine l'upload
Read-Host "`nAppuyez sur Entrée une fois que vous avez terminé l'upload des fichiers"

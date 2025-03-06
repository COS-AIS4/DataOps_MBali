import os

def clean_large_files():
    # Définir la taille limite (ex: 100 Mo)
    taille_limite = 100 * 1024 * 1024  # 100 Mo en octets

    # Répertoire des fichiers à vérifier
    dossier = "data"

    # Vérifier et supprimer les fichiers trop volumineux
    for fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, fichier)
        if os.path.isfile(chemin_fichier) and os.path.getsize(chemin_fichier) > taille_limite:
            os.remove(chemin_fichier)
            print(f"🗑️ Fichier supprimé : {chemin_fichier} (taille > 100 Mo)")
    
    print("✅ Nettoyage terminé.")



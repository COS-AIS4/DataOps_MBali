# Importation des scripts nécessaires
from scripts import fetch_data
from scripts import benchmark
from scripts import visualize_data
from scripts import clean_data

def main():
    print("Démarrage du pipeline DataOps...")
    
    # 1. Exécution de la collecte des données
    print("Récupération des données météo...")
    fetch_data.fetch_weather_data()

    # 2. Exécution des benchmarks
    print("Exécution des benchmarks...")
    benchmark.benchmark_transformation()

    # 3. Génération des visualisations
    print("Génération des visualisations...")
    visualize_data.generate_visualization()

    # 4. Nettoyage des fichiers
    print("Nettoyage des fichiers...")
    clean_data.clean_large_files()

    print("Pipeline DataOps terminé avec succès.")

if __name__ == "__main__":
    main()


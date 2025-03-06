import time
import pandas as pd

def benchmark_transformation():
    start_time = time.time()

    # Charger un fichier CSV
    df = pd.read_csv("data/mon_fichier.csv")

    # Appliquer une transformation (par exemple, multiplier une colonne)
    df["new_col"] = df["old_col"] * 2

    end_time = time.time()

    # Calculer le temps d'exécution
    execution_time = end_time - start_time
    print(f"Temps d'exécution de la transformation : {execution_time:.4f} secondes")

    # Retourner le DataFrame transformé si nécessaire
    return df


import time
import pandas as pd

start_time = time.time()
df = pd.read_csv("data/mon_fichier.csv")  # Simulation de transformation
df["new_col"] = df["old_col"] * 2
end_time = time.time()

print(f"⏱️ Temps d'exécution : {end_time - start_time:.4f} secondes")


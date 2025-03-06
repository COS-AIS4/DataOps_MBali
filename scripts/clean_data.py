import pandas as pd
import pyarrow.parquet as pq

df = pd.read_csv("data/mon_fichier.csv")
df.dropna(inplace=True)  # Suppression des valeurs manquantes
df.to_parquet("data/mon_fichier.parquet", engine="pyarrow")

print("✅ Fichier compressé en Parquet : data/mon_fichier.parquet")


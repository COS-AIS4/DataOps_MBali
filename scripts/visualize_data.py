import matplotlib.pyplot as plt
import json

def generate_visualization():
    # Charger les données météo depuis le fichier JSON
    with open("data/weather.json", "r", encoding="utf-8") as f:
        weather_data = json.load(f)  # Charger le fichier JSON

    # Vérifier si la structure attendue est bien présente
    if "daily" not in weather_data or "time" not in weather_data["daily"] or "temperature_2m_max" not in weather_data["daily"]:
        raise ValueError("❌ Erreur : Le fichier JSON ne contient pas les données météo attendues.")

    # Extraction des données
    dates = weather_data["daily"]["time"]
    temperatures = weather_data["daily"]["temperature_2m_max"]

    # Création du graphique
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker="o", label="Température Max", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.title("Évolution de la température sur 7 jours")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarde du graphique
    plt.savefig("reports/weather_chart.png")
    print("✅ Graphique enregistré dans reports/weather_chart.png")



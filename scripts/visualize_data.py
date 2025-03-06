import matplotlib.pyplot as plt
import json

with open("data/weather.json") as f:
    data = json.load(f)

dates = data["daily"]["time"]
temp_max = data["daily"]["temperature_2m_max"]

plt.figure(figsize=(10,5))
plt.plot(dates, temp_max, marker="o", linestyle="-", color="b", label="Température Max")
plt.xlabel("Date")
plt.ylabel("Température (°C)")
plt.title("Évolution des températures")
plt.legend()
plt.grid()
plt.savefig("reports/weather_chart.png")  
print("✅ Graphique enregistré dans reports/weather_chart.png")


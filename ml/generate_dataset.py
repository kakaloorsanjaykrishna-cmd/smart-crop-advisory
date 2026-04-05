import pandas as pd
import random

# Crop-specific realistic ranges
crop_conditions = {
    "rice":        {"temp": (20, 35), "humidity": (70, 90), "rainfall": (150, 300), "ph": (5.5, 7.0)},
    "wheat":       {"temp": (10, 25), "humidity": (40, 60), "rainfall": (50, 120),  "ph": (6.0, 7.5)},
    "maize":       {"temp": (18, 30), "humidity": (50, 70), "rainfall": (60, 150),  "ph": (5.5, 7.5)},
    "cotton":      {"temp": (25, 40), "humidity": (40, 60), "rainfall": (50, 100),  "ph": (5.5, 8.0)},
    "sugarcane":   {"temp": (20, 35), "humidity": (60, 85), "rainfall": (100, 200), "ph": (6.0, 7.5)},
    "barley":      {"temp": (10, 25), "humidity": (30, 50), "rainfall": (40, 100),  "ph": (6.0, 7.5)},
    "millet":      {"temp": (20, 35), "humidity": (30, 50), "rainfall": (30, 90),   "ph": (5.0, 7.0)},
    "soybean":     {"temp": (20, 30), "humidity": (60, 80), "rainfall": (80, 150),  "ph": (6.0, 7.5)},
    "groundnut":   {"temp": (25, 35), "humidity": (50, 70), "rainfall": (50, 120),  "ph": (6.0, 7.5)},
    "peas":        {"temp": (10, 25), "humidity": (50, 70), "rainfall": (60, 120),  "ph": (6.0, 7.5)}
}

data = []

for _ in range(3000):  # number of rows
    crop = random.choice(list(crop_conditions.keys()))
    cond = crop_conditions[crop]

    N = random.randint(0, 140)
    P = random.randint(5, 145)
    K = random.randint(5, 205)

    temperature = round(random.uniform(*cond["temp"]), 2)
    humidity = round(random.uniform(*cond["humidity"]), 2)
    ph = round(random.uniform(*cond["ph"]), 2)
    rainfall = round(random.uniform(*cond["rainfall"]), 2)

    data.append([N, P, K, temperature, humidity, ph, rainfall, crop])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "N", "P", "K", "temperature", "humidity", "ph", "rainfall", "label"
])

# Save dataset
df.to_csv("crop_recommendation.csv", index=False)

print("✅ Realistic dataset generated successfully!")
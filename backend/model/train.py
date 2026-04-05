import os
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# ✅ Get project root directory (no path issues)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, 'ml', 'dataset', 'crop_recommendation.csv')

print("📂 Loading dataset from:", DATA_PATH)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("✅ Dataset loaded successfully!")
print(df.head())

# Features & target
X = df.drop('label', axis=1)
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")

# Save model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'crop_model.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

pickle.dump(model, open(MODEL_PATH, 'wb'))
pickle.dump(scaler, open(SCALER_PATH, 'wb'))

print("✅ Model & Scaler saved successfully!")
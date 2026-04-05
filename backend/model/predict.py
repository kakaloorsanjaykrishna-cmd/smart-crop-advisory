import pickle
import numpy as np
from app.config import Config

# Load model & scaler
try:
    model = pickle.load(open(Config.MODEL_PATH, 'rb'))
    scaler = pickle.load(open(Config.SCALER_PATH, 'rb'))
except:
    model = None
    scaler = None

def predict_crop(features):
    if model is None or scaler is None:
        return "Model not trained"

    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)

    prediction = model.predict(features)[0]
    return prediction
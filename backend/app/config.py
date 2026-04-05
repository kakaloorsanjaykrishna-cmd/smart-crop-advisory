import os

class Config:
    MODEL_PATH = os.path.join('model', 'crop_model.pkl')
    SCALER_PATH = os.path.join('model', 'scaler.pkl')
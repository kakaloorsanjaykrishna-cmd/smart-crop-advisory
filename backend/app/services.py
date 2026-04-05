from model.predict import predict_crop
from utils.validators import validate_input

def predict_crop_service(data):
    # Validate input
    valid, message = validate_input(data)
    if not valid:
        return {"error": message}

    # Extract features
    features = [
        data['N'],
        data['P'],
        data['K'],
        data['temperature'],
        data['humidity'],
        data['ph'],
        data['rainfall']
    ]

    # Predict
    prediction = predict_crop(features)

    return {
        "recommended_crop": prediction
    }
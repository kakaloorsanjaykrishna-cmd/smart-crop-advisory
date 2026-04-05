from flask import Blueprint, request, jsonify
from app.services import predict_crop_service

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "🌾 Smart Crop Advisory API Running"

@main.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = predict_crop_service(data)
    return jsonify(result)
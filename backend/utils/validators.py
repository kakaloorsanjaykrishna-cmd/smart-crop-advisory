def validate_input(data):
    required_fields = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"

    return True, "Valid input"
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_type(data):
    expected_types = {
        'Age': int,
        'Gender': int,
        'Marital Status': int,
        'Occupation': int,
        'Educational Qualifications': int,
        'Family size': int,
        'latitude': float,
        'longitude': float,
        'Pin code': int
    }
    
    incorrect_types = {
        feature: type(value) for feature, value in data.items()
        if not isinstance(value, expected_types.get(feature, type(value)))
    }
    
    if incorrect_types:
        error_message = ', '.join([
            f'{feature} should be {expected_types[feature]}, got {value_type.__name__}'
            for feature, value_type in incorrect_types.items()
        ])
        return False, error_message
    
    return True, ""


@app.route('/')
def hello_world():
    return jsonify(message="Hello, MLops!")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    required_features = [
        'Age', 'Gender', 'Marital Status', 'Occupation',
        'Educational Qualifications', 'Family size', 'latitude', 'longitude', 'Pin code'
    ]
    
    missing_features = [
        feature for feature in required_features if feature not in data
    ]
    
    if missing_features:
        return jsonify({'error': 'Missing features: ' + ', '.join(missing_features)}), 400

    valid, error_message = is_valid_type(data)
    if not valid:
        return jsonify({'error': error_message}), 400

    # Mock prediction for demonstration purposes
    return jsonify({'Prediction': 1})

if __name__ == '__main__':
    app.run(debug=True)

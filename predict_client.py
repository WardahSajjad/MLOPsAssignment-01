import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Age': 25,  # Example age
    'Gender': 0,
    'Marital Status': 1,
    'Occupation': 2,  # Assuming 2 represents the encoded value for occupation
    'Monthly Income': 3000,  # Example monthly income
    'Educational Qualifications': 3,
    'Family size': 4,  # Example family size
    'Pin code': 560001,  # Example Pin code
    'latitude': 12.9716,  # Example latitude of a location
    'longitude': 77.5946,  # Example longitude of a location
    # 'Output': Not included in prediction request
    # 'Feedback': Not included in prediction request
}

response = requests.post(url, json=data)
print(response.json())

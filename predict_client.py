import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Age': 25,  # Example age
    'Gender': 0,  # Assuming 0 represents the encoded value for gender
    'Marital Status': 1,  # Assuming 1 represents the encoded value for marital status
    'Occupation': 2,  # Assuming 2 represents the encoded value for occupation
    # Removed 'Monthly Income' based on the revised application structure
    'Educational Qualifications': 3,  # Assuming 3 represents the encoded value for educational qualifications
    'Family size': 4,  # Example family size
    'Pin code': 560001,  # Example Pin code
    'latitude': 12.9716,  # Example latitude of a location
    'longitude': 77.5946,  # Example longitude of a location
    # 'Output': Not included in prediction request
    # 'Feedback': Not included in prediction request
}

response = requests.post(url, json=data)
print(response.json())

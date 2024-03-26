import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
# Load the dataset
data = pd.read_csv("onlinefoods.csv")

# testing for workflow

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Check data types and basic statistics
print(data.info())
print(data.describe())

# Replace non-numeric values in "Monthly Income" with NaN
data['Monthly Income'] = pd.to_numeric(data['Monthly Income'], errors='coerce')

# Impute missing values with median
imputer = SimpleImputer(strategy='median')
data['Monthly Income'] = imputer.fit_transform(data[['Monthly Income']])

# Encode categorical variables
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Marital Status'] = label_encoder.fit_transform(data['Marital Status'])
data['Occupation'] = label_encoder.fit_transform(data['Occupation'])
data['Educational Qualifications'] = label_encoder.fit_transform(data['Educational Qualifications'])
data['Output'] = label_encoder.fit_transform(data['Output'])

# Drop irrelevant columns
data.drop(columns=['Feedback', 'Unnamed: 12'], inplace=True)

# Split the data into features and target variable
X = data.drop(columns=['Output'])
y = data['Output']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict on the testing set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

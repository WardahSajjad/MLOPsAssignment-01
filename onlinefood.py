import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, \
    classification_report, confusion_matrix
from joblib import dump

# Load the dataset
data = pd.read_csv("onlinefoods.csv")

print(data.head())

# Check for missing values
print(data.isnull().sum())

# Check data types and basic statistics
print(data.info())
print(data.describe())

data['Monthly Income'] = pd.to_numeric(data['Monthly Income'], errors='coerce')

# Check for missing values in 'Monthly Income' column after conversion
print("Missing values after conversion:")
print(data['Monthly Income'].isnull().sum())

# Apply imputation
imputer = SimpleImputer(strategy='median')
data['Monthly Income'] = imputer.fit_transform(data[['Monthly Income']])
label_encoder = LabelEncoder()
for column in ['Gender', 'Marital Status', 'Occupation',
'Educational Qualifications', 'Output']:
    data[column] = label_encoder.fit_transform(data[column])

# Drop irrelevant columns
data.drop(columns=['Feedback', 'Unnamed: 12'],
        inplace=True)

# Prepare data for modeling
X = data.drop(columns=['Output'])
y = data['Output']
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
# Save the model
model_filename = 'rf_classifier.joblib'

dump(rf_classifier, model_filename)
print(f"Model saved to {model_filename}")

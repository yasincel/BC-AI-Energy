# Cell 1: Loading Trained Model
import joblib

# Load the trained model
model = joblib.load('BIMAIProject/models/linear_regression_model.joblib')

# Cell 2: Import necessary libraries and load data (if not already loaded)
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the processed data (you might need to adjust the path)
processed_data = pd.read_csv('BIMAIProject/data/processed_data.csv')

# Assume 'Electric' is the target variable, and others are features
features = ['Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']
target = 'Electric'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_data[features], processed_data[target], test_size=0.2, random_state=42)

# Cell 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

# Make predictions on the test set
y_pred = model.predict(X_test)

# Example: Create a scatter plot of actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Energy Consumption')
plt.ylabel('Predicted Energy Consumption')
plt.title('Actual vs. Predicted Energy Consumption')
plt.show()

# Additional Cell: Evaluate and Print Metrics
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the processed data
processed_data = pd.read_csv('BIMAIProject/data/processed_data.csv')

# Assume 'Electric' is the target variable, and others are features
features = ['Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']
target = 'Electric'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(processed_data[features], processed_data[target], test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save the trained model
model_dir = 'BIMAIProject/models/'
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'linear_regression_model.joblib')
joblib.dump(model, model_path)

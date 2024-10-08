import joblib

# Load the trained model
model = joblib.load('BIMAIProject/models/linear_regression_model.joblib')

# Cell 2: Making Predictions
# Assuming you have new data in a DataFrame called 'new_data'
predictions = model.predict(new_data)

# Cell 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Create a scatter plot of actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Energy Consumption')
plt.ylabel('Predicted Energy Consumption')
plt.title('Actual vs. Predicted Energy Consumption')
plt.show()

# Cell 4: Further Analysis (if needed)

# Cell 5: Documentation and Explanation
# Use Markdown cells to document your analysis, insights, and explanations.

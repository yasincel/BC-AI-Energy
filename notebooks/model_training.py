import joblib
from BIMAIProject.src.blockchain_integration import Blockchain

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
joblib.dump(model, 'BIMAIProject/models/linear_regression_model.joblib')

# Create a blockchain instance
blockchain = Blockchain()

# Add new setpoints to the blockchain
electric_setpoint = 100.0  # Replace with the actual electric setpoint
boiler_setpoint = 70.0
ventilation_setpoint = 3.0
blockchain.add_setpoints(electric_setpoint, boiler_setpoint, ventilation_setpoint)

# Create a new block with the current setpoints
new_block = blockchain.new_block(previous_hash=None)

# Print the blockchain
for block in blockchain.chain:
    print(block)

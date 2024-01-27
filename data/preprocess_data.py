import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load the raw data
raw_data = pd.read_csv('BIMAIProject/data/raw_data.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')
processed_data = raw_data.copy()
processed_data[['Electric', 'Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']] = imputer.fit_transform(processed_data[['Electric', 'Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']])

# Normalize numeric features
scaler = StandardScaler()
processed_data[['Electric', 'Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']] = scaler.fit_transform(processed_data[['Electric', 'Humidity', 'Temperature', 'CO2_Concentration', 'Boiler_Setpoint', 'Ventilation_Setpoint']])

# Save the processed data to a new CSV file
processed_data.to_csv('BIMAIProject/data/processed_data.csv', index=False)

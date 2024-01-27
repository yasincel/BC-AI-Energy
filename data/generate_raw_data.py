import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the project directory
project_directory = 'BIMAIProject'
data_directory = os.path.join(project_directory, 'data')

# Create directories if they don't exist
os.makedirs(data_directory, exist_ok=True)

# Set a seed for reproducibility
np.random.seed(42)

# Generate synthetic data for the IoT parameters
num_records = 1000

start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=num_records - 1)

date_range = pd.date_range(start=start_date, end=end_date, freq='D')

data = {
    'Date': date_range,
    'Electric': np.random.uniform(50, 150, num_records),
    'Humidity': np.random.uniform(30, 70, num_records),
    'Temperature': np.random.uniform(18, 28, num_records),
    'CO2_Concentration': np.random.uniform(300, 800, num_records),
    'Boiler_Setpoint': np.random.uniform(65, 75, num_records),
    'Ventilation_Setpoint': np.random.uniform(1, 5, num_records),
}

# Create a DataFrame
raw_data = pd.DataFrame(data)

# Save the raw data to a CSV file
raw_data.to_csv(os.path.join(data_directory, 'raw_data.csv'), index=False)

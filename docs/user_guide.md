# BIMAI Project User Guide

Welcome to the BIMAI project created by YC at Cardiff University! This guide will help you understand how to use the linear regression model for predicting energy consumption and interpret the blockchain data.

## Linear Regression Model

### Installation

To use the linear regression model, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the required dependencies by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Load the trained linear regression model:

    ```python
    import joblib

    # Load the trained model
    model = joblib.load('BIMAIProject/models/linear_regression_model.joblib')
    ```

2. Make predictions using the model:

    ```python
    # Assuming 'X_new' is a DataFrame with new data
    predictions = model.predict(X_new)
    ```

### Evaluation

After making predictions, you can evaluate the model's performance using metrics such as Mean Squared Error (MSE) and R-squared.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Calculate evaluation metrics
mse = mean_squared_error(y_true, predictions)
r2 = r2_score(y_true, predictions)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

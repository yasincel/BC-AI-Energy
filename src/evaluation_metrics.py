from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the linear regression model and print the metrics.

    Parameters:
    - model: Trained linear regression model
    - X_test: Test set features
    - y_test: Test set target variable
    """
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print the metrics
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

if __name__ == '__main__':
    # Assuming you have the model loaded and test set (X_test, y_test) prepared
    # Load the trained model
    # model = joblib.load('BIMAIProject/models/linear_regression_model.joblib')

    # Assuming you have the X_test, y_test prepared
    # Evaluate the model
    # evaluate_model(model, X_test, y_test)

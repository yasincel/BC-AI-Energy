##BIMAI Project Report

##Introduction

The BIMAI project created by YC at Cardiff University aims to address energy optimization in buildings using artificial intelligence (AI) techniques. The primary objective is to develop a predictive model for energy consumption, leveraging machine learning algorithms to improve efficiency and sustainability in building operations.

##Data Collection

The data sources for the project include sensor readings from various building systems such as temperature, humidity, CO2 concentration, boiler temperature set point, and air ventilation set point. The raw data is collected in CSV format from sensors installed throughout the building. Preprocessing steps involve cleaning the data, handling missing values, and formatting it for analysis.

##Data Exploration

Exploratory data analysis reveals patterns, trends, and anomalies within the dataset. Visualizations are employed to identify correlations between variables, detect outliers, and understand the distribution of data.

##Data Preprocessing

Preprocessing steps include handling missing values through imputation techniques, identifying and removing outliers, and scaling or normalizing the data for model training. Additionally, feature engineering may be performed to create new variables or transform existing ones to improve model performance.

##Linear Regression Model

The linear regression model is utilized to predict energy consumption based on features such as indoor temperature, humidity, CO2 concentration, boiler temperature set point, and air ventilation set point. The model is trained using historical data, and coefficients are learned to estimate energy consumption accurately.

##Model Evaluation

Evaluation metrics such as Mean Squared Error (MSE) and R-squared are employed to assess the performance of the linear regression model. These metrics provide insights into the model's predictive accuracy and its ability to explain variance in the data.

##Blockchain Integration

Blockchain technology is integrated into the project to ensure transparency and immutability of energy optimization parameters. Setpoints for boiler temperature and air ventilation are recorded in the blockchain, creating an auditable and secure record of key parameters.

##Blockchain Evaluation

To ensure the integrity of the blockchain, mechanisms such as consensus algorithms and cryptographic hashing are utilized. These mechanisms verify the recorded setpoints and prevent tampering or unauthorized modifications.

##User Guide

A user guide is provided to assist stakeholders in using the linear regression model for energy consumption prediction and interpreting blockchain data. It includes instructions on model deployment, input requirements, and accessing blockchain records.

##Conclusion

The project demonstrates the effectiveness of AI techniques in optimizing energy consumption in buildings. Key findings include the importance of data preprocessing, the predictive power of linear regression models, and the benefits of blockchain integration for data integrity.

##Future Work

Future iterations of the project could focus on enhancing model performance through advanced machine learning algorithms or exploring additional features for prediction. Improvements in blockchain technology and integration with smart building systems could further enhance energy optimization capabilities.

##References

[1] Python Documentation: https://www.python.org/doc/
[2] Scikit-learn Documentation: https://scikit-learn.org/stable/documentation.html
[3] Ethereum Documentation: https://ethereum.org/en/developers/docs/

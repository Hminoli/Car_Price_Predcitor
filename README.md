# Car Price Prediction Using Machine Learning

## Overview

This project aims to predict the selling price of cars based on various features such as brand, model, year, mileage, fuel type, and other specifications. By leveraging machine learning models, the system provides accurate price estimates that can assist buyers and sellers in making informed decisions.

## Dataset

The dataset used in this project contains information about cars, including:

- Year of manufacture  
- Mileage  
- Fuel type  
- Transmission type  
- Engine capacity  
- Owner type
- Brand
- Color
- Service history
- Accidents reported 
- Selling price (target variable)  

## Problem Statement

The goal is to build a machine learning model that can accurately estimate the selling price of a car based on its features. Accurate price predictions can help prevent overpricing or undervaluation in the used car market.

## Methods Used

- **Data Preprocessing**:  
  - Handled missing values  
  - Encoded categorical variables  

- **Machine Learning Models**:  
  - Linear Regression  
  - Decision Tree Regressor
  - Bagging Regressor
  - AdaBoost Regressor
  - Random Forest Regressor  
  - Support vector machine

- **Model Selection**: Compared different regression models to find the best-performing one.

## Evaluation Metrics

Models were evaluated using the following metrics:

- R² Score  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  

## Key Findings

- **Linear Regression** achieved an R² score of **0.8696**, MSE of **998,642.69**, and RMSE of **999.32**.  
- Key features influencing car price included:  
  - Year of manufacture  
  - Mileage  
  - Fuel type  
  - Transmission type  

## Conclusion

This project demonstrates how machine learning can be used to predict car prices effectively. Such a model can be integrated into online platforms to assist in setting competitive prices for used cars.

## Tools and Technologies

- Python  
- Flask (for web app deployment)  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- HTML, CSS (for frontend)  

## Author

W. A. D. Himansa Minoli  
University of Colombo  
BSc Honours in Applied Statistics

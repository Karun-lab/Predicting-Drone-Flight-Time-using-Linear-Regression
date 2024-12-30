# Predicting-Drone-Flight-Time-using-Linear-Regression
This repository demonstrates how to use linear regression to predict drone flight time based on payload weight. It includes a Python implementation using scikit-learn and matplotlib.

## Features
- Predict flight time for different payload weights.
- Visualize data and the best-fit line.

## Getting Started
1. Clone the repository:
```
https://github.com/Karun-lab/Predicting-Drone-Flight-Time-using-Linear-Regression.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run program
```
payload-prediction.py
```
## Explanation
Suppose you want to predict the flight time of a drone (Y) based on its payload weight (X).

Data Collection:
Collect data on flight times (Y) for different payloads (X).

Example:
    Payload (kg):[0.5,1.0,1.5,2.0,2.5]
    Flight Time (min):[30,25,20,15,10]

Fit the Model:
    Calculate β0​ (intercept) and β1 (slope).
    Use the least squares method to minimize the error:
The general form of the linear regression equation is:

$$
y = \beta_0 + \beta_1 x
$$

Where:
- \( y \) is the dependent variable (the predicted value).
- \( x \) is the independent variable (the input feature).
- \( \beta_0 ) is the intercept (the value of \( y \) when \( x = 0 \)).
- \( \beta_1 ) is the slope (the change in \( y \) for a unit change in \( x \)).

## Least Squares Method for Linear Regression

The least squares method aims to minimize the sum of squared errors (residuals):

$$
E = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2
$$

Where:
- \( E \) is the error function.
- \( y_i \) is the actual value for the \(i\)-th data point.
- \( x_i \) is the input feature for the \(i\)-th data point.
- \( n \) is the number of data points.

To solve for the best-fit parameters, we use the following normal equations:

$$
\beta_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}
$$

$$
\beta_0 = \frac{\sum y_i - \beta_1 \sum x_i}{n}
$$
Prediction:
    With the equation Y=β0+β1XY=β0​+β1​X, predict flight time for a new payload.

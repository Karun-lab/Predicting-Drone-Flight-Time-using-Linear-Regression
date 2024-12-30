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

Data Collection:<br/>
Collect data on flight times (Y) for different payloads (X).

Example:<br/>
    Payload (kg):[0.5,1.0,1.5,2.0,2.5] <br/>
    Flight Time (min):[30,25,20,15,10]

Fit the Model:<br/>
Calculate β0​ (intercept) and β1 (slope).Use the least squares method to minimize the error.<br/>
The general form of the linear regression equation is:

$$
y = \beta_0 + \beta_1 x
$$

Where:
- \( y \) is the dependent variable (the predicted value).
- \( x \) is the independent variable (the input feature).
- β0 is the intercept (the value of \( y \) when \( x = 0 \)).
- β1 is the slope (the change in \( y \) for a unit change in \( x \)).



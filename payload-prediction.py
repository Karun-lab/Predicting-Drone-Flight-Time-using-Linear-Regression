#Predicting Drone Flight Time using Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
payload = np.array([0.5, 1.0, 1.5, 2.0, 2.5]).reshape(-1, 1)  # Independent variable (X)
flight_time = np.array([30, 25, 20, 15, 10])  # Dependent variable (Y)

# Fit the model
model = LinearRegression()
model.fit(payload, flight_time)

# Predictions
new_payload = np.array([3.0]).reshape(-1, 1)  # Predict for a payload of 3.0 kg
predicted_time = model.predict(new_payload)

# Print results
print("Intercept (β0):", model.intercept_)
print("Slope (β1):", model.coef_[0])
print(f"Predicted flight time for 3.0 kg: {predicted_time[0]:.2f} minutes")

# Plot
plt.scatter(payload, flight_time, color='blue', label='Data Points')
plt.plot(payload, model.predict(payload), color='red', label='Best Fit Line')
plt.xlabel('Payload (kg)')
plt.ylabel('Flight Time (min)')
plt.legend()
plt.show()

from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Create a SVR model with a gaussian kernel
model = SVR(kernel='rbf')

# Fit the model to the data
model.fit(X, y)

# Predict the output for the input data
y_pred = model.predict(X)

# Calculate the mean squared error
mse = mean_squared_error(y, y_pred)

print("Mean Squared Error:", mse)

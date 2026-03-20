from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Create a pipeline with a scaler and an SVR
model = make_pipeline(StandardScaler(), SVR(kernel='poly', degree=2))

# Fit the model to the data
model.fit(X, y)

# Predict the output
y_pred = model.predict(X)

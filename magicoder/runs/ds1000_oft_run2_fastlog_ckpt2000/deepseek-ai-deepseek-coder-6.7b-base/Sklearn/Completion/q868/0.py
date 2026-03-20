from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X, y)
predicted = regressor.predict(X)

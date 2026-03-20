from sklearn.svm import SVR
regressor = SVR(kernel='poly', degree=2)
regressor.fit(X, y)
predictions = regressor.predict(X)

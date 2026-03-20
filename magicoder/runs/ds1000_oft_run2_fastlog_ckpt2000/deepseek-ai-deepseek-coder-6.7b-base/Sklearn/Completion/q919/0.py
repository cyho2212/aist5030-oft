logReg = LogisticRegression()
X = dataframe.iloc[:, :-1].astype(float)
y = dataframe.iloc[:, -1]
logReg.fit(X, y)
predict = logReg.predict(X)

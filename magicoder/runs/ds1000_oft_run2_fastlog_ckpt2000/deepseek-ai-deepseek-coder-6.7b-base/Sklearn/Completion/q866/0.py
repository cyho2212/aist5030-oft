X_train = pd.get_dummies(X_train[0])
X_train = X_train.join(X_train.drop(0, axis=1))

# Model.
clf = GradientBoostingClassifier(learning_rate=0.01,max_depth=8,n_estimators=50).fit(X_train, y_train)

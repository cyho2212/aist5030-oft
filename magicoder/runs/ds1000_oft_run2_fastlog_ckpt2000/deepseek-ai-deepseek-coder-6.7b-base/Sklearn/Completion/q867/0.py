X_train = pd.get_dummies(X_train[0])
X_train = X_train.join(X_train.drop(columns=[0]))

# train model
clf = GradientBoostingClassifier(learning_rate=0.01,max_depth=8,n_estimators=50).fit(X_train, y_train)

selector = sklearn.feature_selection.SelectFromModel(LinearSVC(penalty='l1', dual=False))
selector.fit(X, y)
selected_feature_names = np.asarray(vectorizer.get_feature_names())[selector.get_support()]

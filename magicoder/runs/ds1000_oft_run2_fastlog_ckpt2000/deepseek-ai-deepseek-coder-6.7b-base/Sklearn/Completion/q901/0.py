    clf = LinearSVC(penalty='l1', dual=False).fit(X, y)
    selected_features = np.asarray(vectorizer.get_feature_names())[clf.coef_[0] != 0]
    return selected_features

selected_features = solve(corpus, y, vectorizer, X)
print(selected_features)

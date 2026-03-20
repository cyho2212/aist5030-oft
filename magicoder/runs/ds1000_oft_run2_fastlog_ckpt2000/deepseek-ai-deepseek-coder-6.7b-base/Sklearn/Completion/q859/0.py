column_names = X.columns[clf.feature_importances_ > 0]
print(column_names)

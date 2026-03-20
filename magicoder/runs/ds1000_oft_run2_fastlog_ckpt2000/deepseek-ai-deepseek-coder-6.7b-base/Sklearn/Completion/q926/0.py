count = CountVectorizer(lowercase = False)
vocabulary = count.fit_transform([words])
feature_names = count.get_feature_names()
print(feature_names)

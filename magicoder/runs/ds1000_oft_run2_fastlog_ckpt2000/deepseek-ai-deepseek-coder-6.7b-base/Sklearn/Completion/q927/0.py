count = CountVectorizer(lowercase = False)
vocabulary = count.fit_transform([words])
feature_names = count.get_feature_names_out()
print(feature_names)

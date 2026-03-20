vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w\w+\b", lowercase=False)
transformed_text = vectorizer.fit_transform([text])

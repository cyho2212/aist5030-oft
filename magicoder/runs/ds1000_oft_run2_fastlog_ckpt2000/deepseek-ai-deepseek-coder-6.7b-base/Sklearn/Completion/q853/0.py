def prePro(text):
    return text.lower()

tfidf = TfidfVectorizer(preprocessor=prePro)

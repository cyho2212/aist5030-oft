
# Define the preprocessing function
def preprocess(s):
    return s.upper()

# Create a TfidfVectorizer object
tfidf = TfidfVectorizer(preprocessor=preprocess)

# Fit the vectorizer to some sample data
tfidf.fit(["hello world", "goodbye world"])

# Transform the data
X = tfidf.transform(["hello world", "goodbye world"])

# Print the transformed data
print(X.toarray())

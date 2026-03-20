cosine_similarities_of_queries = []
for query in queries:
    query_vector = tfidf.transform([query])
    cosine_similarities = np.dot(query_vector, tfidf.transform(documents).T).toarray()[0]
    cosine_similarities_of_queries.append(cosine_similarities)

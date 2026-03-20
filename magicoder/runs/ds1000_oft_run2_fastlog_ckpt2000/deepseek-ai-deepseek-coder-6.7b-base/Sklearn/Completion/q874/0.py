    query_vectors = tfidf.transform(queries)
    doc_vectors = tfidf.transform(documents)
    similarity_matrix = np.dot(query_vectors, doc_vectors.T).toarray()
    return similarity_matrix

print(solve(queries, documents))

tfidf_matrix = tfidf.fit_transform(df['description'])
cosine_similarity_matrix = sklearn.metrics.pairwise.cosine_similarity(tfidf_matrix)
similarity_df = pd.DataFrame(cosine_similarity_matrix, index=df['items'], columns=df['items'])
print(similarity_df)

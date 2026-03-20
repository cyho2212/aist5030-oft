X = df['mse'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=2, n_init=10).fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

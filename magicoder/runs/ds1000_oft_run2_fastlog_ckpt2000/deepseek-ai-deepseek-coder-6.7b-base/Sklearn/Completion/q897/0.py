labels = KMeans(n_clusters=2, n_init=10).fit_predict(df['mse'].values.reshape(-1, 1))

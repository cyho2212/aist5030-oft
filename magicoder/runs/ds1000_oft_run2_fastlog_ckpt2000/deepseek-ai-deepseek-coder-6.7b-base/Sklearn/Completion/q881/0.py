
# Convert the distance matrix to a condensed distance vector
condensed_distance_vector = np.triu(data_matrix, k=1).flatten()

# Perform hierarchical clustering
cluster_labels = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete').fit_predict(condensed_distance_vector)

# Print the cluster labels
print(cluster_labels)

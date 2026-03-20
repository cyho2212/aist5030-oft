
# Convert the data matrix to a distance matrix
distance_matrix = 1 - data_matrix

# Perform hierarchical clustering
cluster = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = cluster.fit_predict(distance_matrix)

# Print the cluster labels
print(cluster_labels)

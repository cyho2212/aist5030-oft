
# Convert the similarity matrix to a distance matrix
distM = 1 - simM

# Perform hierarchical clustering
clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = clustering.fit_predict(distM)

# Print the cluster labels
print(cluster_labels)

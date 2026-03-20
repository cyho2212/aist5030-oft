from scipy.cluster.hierarchy import linkage, fcluster

# Perform hierarchical clustering
Z = linkage(data_matrix, 'ward')

# Cut the dendrogram to obtain the clusters
cluster_labels = fcluster(Z, 2, criterion='maxclust')

# Print the cluster labels
print(cluster_labels)

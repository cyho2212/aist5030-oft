from scipy.cluster.hierarchy import linkage, fcluster

# Perform hierarchical clustering
Z = linkage(simM, 'ward')

# Cluster the data into 2 clusters
cluster_labels = fcluster(Z, 2, criterion='maxclust')

# Print the cluster labels
print(cluster_labels)

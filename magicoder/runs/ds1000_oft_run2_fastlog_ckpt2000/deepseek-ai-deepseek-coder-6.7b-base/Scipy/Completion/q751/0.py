    # Convert 2D array to 1D array
    flat_arr = example_array.flatten()
    # Get unique IDs
    unique_ids = np.unique(flat_arr)
    # Create a dictionary to store distances
    distances = {}
    # Loop through unique IDs
    for i in unique_ids:
        # Get indices of current ID
        indices = np.where(flat_arr == i)[0]
        # Calculate pairwise distances
        dist = scipy.spatial.distance.pdist(indices.reshape(-1, 1))
        # Add distances to dictionary
        distances[i] = dist
    return distances

print(f())

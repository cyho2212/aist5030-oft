
# Create a boolean mask where True means the value is above the threshold
mask = img > threshold

# Label the connected regions
labels, num_labels = ndimage.label(mask)

# Calculate the center of mass for each region
coms = ndimage.center_of_mass(img, labels, np.arange(1, num_labels + 1))

# Calculate the distance from the center of mass to the top left corner
distances = np.sqrt((coms[:, 0] - 0)**2 + (coms[:, 1] - 0)**2)

# Print the distances
print(distances)


# Convert points to numpy array
points = np.array(points)

# Extract x and y coordinates
x = points[:, 0]
y = points[:, 1]

# Plot the line plot
plt.plot(x, y)

# Set the y-axis to log scale
plt.yscale('log')

# Show the plot
plt.show()

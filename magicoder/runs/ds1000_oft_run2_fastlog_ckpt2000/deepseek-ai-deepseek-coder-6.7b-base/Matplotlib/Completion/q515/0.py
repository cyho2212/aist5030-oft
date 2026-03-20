
# Generate random y values
y = np.random.rand(10)

# Define line styles
styles = ['-', '--', '-.', ':']

# Plot the lines
for style in styles:
    plt.plot(x, y, style)

# Show the plot
plt.show()


# Calculate the slope of the line
slope = (d - b) / (c - a)

# Calculate the y-intercept
y_intercept = b - slope * a

# Create a list of x-values
x_values = [0, 5]

# Calculate the corresponding y-values
y_values = [slope * x + y_intercept for x in x_values]

# Plot the line
plt.plot(x_values, y_values)

# Set the xlim and ylim
plt.xlim(0, 5)
plt.ylim(0, 5)

# Show the plot
plt.show()

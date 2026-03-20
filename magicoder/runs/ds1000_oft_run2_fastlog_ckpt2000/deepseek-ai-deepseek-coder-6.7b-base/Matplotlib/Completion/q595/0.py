
# Calculate the sum of the data
total = sum(data)

# Normalize the data to sum up to 1
normalized_data = [i/total for i in data]

# Create a histogram
plt.hist(normalized_data, bins=len(data))

# Format the y tick labels into percentage and set y tick labels as 10%, 20%, etc.
plt.yticks(np.arange(0, 1.1, 0.1))
plt.yticklabels(['{:,.0%}'.format(x) for x in plt.gca().get_yticks()])

# Show the plot
plt.show()

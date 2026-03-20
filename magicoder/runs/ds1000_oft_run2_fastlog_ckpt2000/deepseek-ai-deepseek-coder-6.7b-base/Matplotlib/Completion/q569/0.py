
# Create a bar plot for s1 and s2
plt.bar(df["celltype"], df["s1"], label="s1")
plt.bar(df["celltype"], df["s2"], label="s2")

# Set the x-axis tick labels to rotate 45 degrees
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Show the plot
plt.show()


# Create a bar plot for s1 and s2
plt.bar(df["celltype"], df["s1"], label="s1")
plt.bar(df["celltype"], df["s2"], label="s2")

# Set the x-axis tick labels horizontal
plt.xticks(rotation=90)

# Add a legend
plt.legend()

# Show the plot
plt.show()

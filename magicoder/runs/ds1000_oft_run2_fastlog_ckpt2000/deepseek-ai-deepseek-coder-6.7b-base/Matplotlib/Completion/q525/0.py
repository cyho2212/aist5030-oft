
# Create a dataframe
df = pd.DataFrame({'x': x, 'y': y})

# Draw a line plot
sns.lineplot(data=df, x='x', y='y')

# Show the plot
plt.show()

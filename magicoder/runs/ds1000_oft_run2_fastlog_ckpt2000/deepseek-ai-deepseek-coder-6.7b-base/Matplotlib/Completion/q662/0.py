g = sns.FacetGrid(df, col="b", hue="b", sharex=False)
g.map(sns.pointplot, "a", "c")

# Set xticks and xtick labels
for ax in g.axes.flat:
    ax.set_xticks(np.arange(1, 31, 2))
    ax.set_xticklabels(np.arange(1, 31, 2))

plt.show()

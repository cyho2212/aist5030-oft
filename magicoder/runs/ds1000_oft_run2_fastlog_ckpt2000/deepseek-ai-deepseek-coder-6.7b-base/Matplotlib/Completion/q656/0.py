sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=df, kind="scatter", legend=False)
plt.ylabel('')
plt.show()

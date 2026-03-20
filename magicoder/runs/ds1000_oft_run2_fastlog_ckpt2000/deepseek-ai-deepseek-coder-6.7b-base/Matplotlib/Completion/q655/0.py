sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=df, kind="scatter")
plt.xlabel("Exercise Time")
plt.ylabel("Exercise Time")
plt.show()

sns.stripplot(data=df, x="sex", y="bill_length_mm", hue="species", dodge=True, jitter=True, legend=False)
plt.show()

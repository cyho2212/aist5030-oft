fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for i, col in enumerate(df.columns):
    ax = axes[i//2, i%2]
    ax.plot(df.index, df[col], 'o-')
    ax.set_title(col)

plt.show()

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, loc='center')
plt.show()

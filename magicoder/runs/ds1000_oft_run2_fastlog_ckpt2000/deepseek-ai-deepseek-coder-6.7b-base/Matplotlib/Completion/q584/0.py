
fig, ax = plt.subplots()

ax.hist(x, alpha=0.5, label='x')
ax.hist(y, alpha=0.5, label='y')

ax.legend()
plt.show()

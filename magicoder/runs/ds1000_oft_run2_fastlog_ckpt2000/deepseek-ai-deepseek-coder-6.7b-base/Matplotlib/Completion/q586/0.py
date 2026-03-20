fig, (ax1, ax2) = plt.subplots(1, 2)

p1 = ax1.imshow(x, cmap='viridis')
p2 = ax2.imshow(y, cmap='viridis')

fig.colorbar(p1, ax=ax1)
fig.colorbar(p2, ax=ax2)

plt.show()

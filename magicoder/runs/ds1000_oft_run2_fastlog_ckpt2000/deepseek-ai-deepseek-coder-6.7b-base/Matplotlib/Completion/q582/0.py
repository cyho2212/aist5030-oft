fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(x, y)
ax1.set_title('Subplot 1')

ax2.plot(x, y)
ax2.set_title('Subplot 2')

plt.tight_layout()
plt.show()

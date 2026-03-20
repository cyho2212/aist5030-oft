fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y, label='y')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()

ax2.plot(z, a, label='a')
ax2.set_xlabel('z')
ax2.set_ylabel('a')
ax2.legend()

plt.tight_layout()
plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y)
ax1.set_title('Y over X')

ax2.plot(a, z)
ax2.set_title('Z over A')

fig.suptitle('Y and Z', fontsize=16)

plt.show()

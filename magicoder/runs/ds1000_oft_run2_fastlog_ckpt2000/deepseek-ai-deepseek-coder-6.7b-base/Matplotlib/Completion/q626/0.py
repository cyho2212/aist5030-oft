fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot y over x in the first subplot
ax[0].plot(x, y, label='y')

# Plot z over a in the second subplot
ax[1].plot(a, z, label='z')

# Put them into a single legend on the first subplot
ax[0].legend()

plt.show()

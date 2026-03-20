gs = gridspec.GridSpec(nrow, ncol)
for i in range(nrow):
    for j in range(ncol):
        ax = plt.subplot(gs[i, j])
        ax.imshow(x)
        ax.set_xticks([])
        ax.set_yticks([])

plt.tight_layout()
plt.show()

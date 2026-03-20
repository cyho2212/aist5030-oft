fig, ax = plt.subplots()
im = ax.imshow(rand_mat)

# We want to show all ticks...
ax.set_xticks(numpy.arange(len(xlabels)))
ax.set_yticks(numpy.arange(len(ylabels)))
# ... and label them with the respective list entries
ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels[::-1])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(xlabels)):
    for j in range(len(ylabels)):
        text = ax.text(j, i, rand_mat[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Heatmap")
fig.tight_layout()
plt.show()

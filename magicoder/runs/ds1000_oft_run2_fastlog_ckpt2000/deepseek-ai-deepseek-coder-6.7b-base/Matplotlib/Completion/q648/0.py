fig, axs = plt.subplots(4, 4, figsize=(5, 5))
for i in range(4):
    for j in range(4):
        axs[i, j].plot(x, y)
        axs[i, j].set_xticks(x)
        axs[i, j].set_yticks(y)
        axs[i, j].set_xlabel('x')
        axs[i, j].set_ylabel('y')
        axs[i, j].set_title('Subplot ' + str(i+1) + ',' + str(j+1))
plt.tight_layout()
plt.show()

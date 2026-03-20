for i in range(len(box_position)):
    ax.errorbar(box_position[i], box_height[i], yerr=box_errors[i], color=c[i], fmt='o')

plt.show()

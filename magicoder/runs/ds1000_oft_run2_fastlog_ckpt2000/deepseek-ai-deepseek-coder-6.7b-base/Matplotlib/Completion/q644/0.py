plt.figure()
plt.errorbar(x, y, yerr=error, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0)
plt.fill_between(x, y-error, y+error, color='lightgray')
plt.show()

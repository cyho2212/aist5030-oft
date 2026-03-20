for i in range(len(lines)):
    x = [lines[i][0][0], lines[i][1][0]]
    y = [lines[i][0][1], lines[i][1][1]]
    plt.plot(x, y, color=c[i])

plt.show()

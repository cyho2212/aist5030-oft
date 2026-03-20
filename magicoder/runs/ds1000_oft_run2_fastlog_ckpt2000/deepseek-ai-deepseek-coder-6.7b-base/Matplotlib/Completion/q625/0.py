x = np.arange(len(blue_bar))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, blue_bar, width, label='Blue')
rects2 = ax.bar(x + width/2, orange_bar, width, label='Orange')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Height')
ax.set_title('Blue and Orange Bars')
ax.set_xticks(x)
ax.set_xticklabels(('Group 1', 'Group 2', 'Group 3'))
ax.legend()

fig.tight_layout()

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y1)
ax1.set_title('Sine Wave')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.plot(x, y2)
ax2.set_title('Cosine Wave')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg", color="green", hist_kws={'color': 'blue'})
plt.show()

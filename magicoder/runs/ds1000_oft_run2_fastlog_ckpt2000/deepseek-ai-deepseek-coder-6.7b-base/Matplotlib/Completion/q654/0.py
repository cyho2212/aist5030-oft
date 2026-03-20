
# Create a new column "group" based on the "diet" column
df['group'] = df['diet'].apply(lambda x: 'Fat' if x == 'yes' else 'No Fat')

# Create a catplot
g = sns.catplot(x="time", y="pulse", hue="kind", col="group", data=df, kind="scatter")

# Change the subplots titles
g.set_titles("{col_name}")

plt.show()

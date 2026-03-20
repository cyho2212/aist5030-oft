
# Create a new column for bill_length_mm in mm
df['bill_length_mm'] = df['bill_length_mm'] * 10

# Create a new column for bill_length_mm in cm
df['bill_length_cm'] = df['bill_length_mm'] / 10

# Plot the barplot
sns.catplot(x="sex", y="bill_length_cm", hue="species", data=df, kind="bar", col="species", sharey=False)

plt.show()

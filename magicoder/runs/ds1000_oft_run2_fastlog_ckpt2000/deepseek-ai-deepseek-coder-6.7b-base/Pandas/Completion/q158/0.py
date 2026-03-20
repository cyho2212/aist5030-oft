
# Create a new column 'Family' based on the conditions
df['Family'] = ((df['Survived'] > 0) | (df['Parch'] > 0)).astype(int)

# Group by 'Family' and calculate the mean of 'SibSp'
result = df.groupby('Family')['SibSp'].mean()

print(result)

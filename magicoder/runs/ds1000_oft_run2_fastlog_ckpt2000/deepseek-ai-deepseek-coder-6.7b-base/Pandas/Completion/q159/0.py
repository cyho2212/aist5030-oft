
# Create a new column 'Family' based on the conditions
df['Family'] = 'No Family'
df.loc[(df['SibSp'] == 1) & (df['Parch'] == 1), 'Family'] = 'Has Family'
df.loc[(df['SibSp'] == 0) & (df['Parch'] == 1), 'Family'] = 'New Family'
df.loc[(df['SibSp'] == 1) & (df['Parch'] == 0), 'Family'] = 'Old Family'

# Group by 'Family' and calculate the mean of 'Survived'
result = df.groupby('Family')['Survived'].mean()

print(result)

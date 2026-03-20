
# Create a new column 'HasFamily' based on the conditions
df['HasFamily'] = ((df['SibSp'] > 0) | (df['Parch'] > 0)).astype(int)

# Group by 'HasFamily' and calculate the mean of 'Survived'
result = df.groupby('HasFamily')['Survived'].mean()

print(result)

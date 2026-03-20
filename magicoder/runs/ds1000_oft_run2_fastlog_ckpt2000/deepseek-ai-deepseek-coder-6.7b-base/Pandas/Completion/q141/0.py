
# Get all column levels
column_levels = df.columns.levels

# Create a list of tuples where each tuple contains the first, second, and third column levels
value_vars = [(column_levels[0][i], column_levels[1][j], column_levels[2][k])
              for i in range(len(column_levels[0]))
              for j in range(len(column_levels[1]))
              for k in range(len(column_levels[2]))]

# Melt the dataframe
result = pd.melt(df, value_vars=value_vars)

print(result)

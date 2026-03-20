
# Create a list of tuples where each tuple is a column level
column_levels = [(col1, col2, col3) for col1, col2, col3 in zip(df.columns[0], df.columns[1], df.columns[2])]

# Melt the dataframe
result = pd.melt(df.reset_index(), id_vars='index', value_vars=column_levels)

# Rename the columns
result.columns = ['index', 'variable_0', 'variable_1', 'variable_2', 'value']

print(result)

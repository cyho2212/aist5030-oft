
# Get the maximum number of rows from all dataframes
max_rows = max(len(df) for df in [a, b])

# Pad all dataframes to the maximum number of rows
a = a.reindex(range(max_rows), fill_value=np.nan)
b = b.reindex(range(max_rows), fill_value=np.nan)

# Create a new dataframe with tuples
result = pd.DataFrame({'one': list(zip(a['one'], b['one'])),
                       'two': list(zip(a['two'], b['two']))})

print(result)

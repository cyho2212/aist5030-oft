
# Get the list of columns that end with '2'
cols_to_mean = [col for col in df.columns if col.endswith('2')]

# Get the list of columns that do not end with '2'
cols_to_sum = [col for col in df.columns if col not in cols_to_mean]

# Group by 'group' and aggregate
result = df.groupby('group').agg({"group_color": "first", **{col: "mean" for col in cols_to_mean}, **{col: "sum" for col in cols_to_sum}})

print(result)

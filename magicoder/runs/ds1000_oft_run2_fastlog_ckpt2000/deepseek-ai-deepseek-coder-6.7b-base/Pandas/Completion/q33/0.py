
# Get all columns that contain 'val' in their names
val_columns = [col for col in df.columns if 'val' in col]

# Group by 'group' and aggregate the mean of all other columns
result = df.groupby('group').agg({"group_color": "first", **{col: "mean" for col in val_columns}})

print(result)

result = df.groupby('group').agg({"group_color": "first", **{col: "sum" for col in df.columns if "val" in col}})
print(result)

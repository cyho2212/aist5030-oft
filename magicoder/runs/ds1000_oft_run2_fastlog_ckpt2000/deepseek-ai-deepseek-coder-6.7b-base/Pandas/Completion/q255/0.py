result = ','.join(str(x) for x in df['col1'].explode().tolist())
print(result)

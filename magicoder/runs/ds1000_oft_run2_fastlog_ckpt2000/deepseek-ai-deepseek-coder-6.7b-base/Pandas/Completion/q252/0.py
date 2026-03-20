result = pd.DataFrame(df['codes'].tolist(), index=df.index).add_prefix('code_')
print(result)

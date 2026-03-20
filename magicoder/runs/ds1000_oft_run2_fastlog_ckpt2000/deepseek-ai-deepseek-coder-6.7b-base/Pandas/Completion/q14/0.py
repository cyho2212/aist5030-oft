df['datetime'] = df['datetime'].dt.tz_localize(None)

# Export to Excel
df.to_excel('output.xlsx', index=False)

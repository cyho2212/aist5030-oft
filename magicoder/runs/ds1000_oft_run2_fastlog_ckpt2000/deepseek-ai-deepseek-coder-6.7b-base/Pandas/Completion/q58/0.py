
# Get the min and max date
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates between min and max
new_df = pd.DataFrame({'dt': pd.date_range(min_date, max_date)})

# Merge the two dataframes
result = pd.merge(new_df, df, on='dt', how='left').fillna(233)

print(result)


# Get the minimum and maximum date
min_date = df['dt'].min()
max_date = df['dt'].max()

# Create a new dataframe with all dates between min_date and max_date
new_df = pd.DataFrame({'dt': pd.date_range(min_date, max_date)})

# Merge the new dataframe with the original dataframe
result = pd.merge(new_df, df, on='dt', how='left')

# Fill the missing values in the 'val' column with the maximum value of 'val' for each 'user'
result['val'] = result.groupby('user')['val'].transform('max')

# Format the 'dt' column
result['dt'] = result['dt'].dt.strftime('%d-%b-%Y')

print(result)

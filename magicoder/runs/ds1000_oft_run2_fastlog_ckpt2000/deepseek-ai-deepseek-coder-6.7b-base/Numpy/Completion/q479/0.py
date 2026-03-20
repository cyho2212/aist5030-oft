start_date = pd.to_datetime(start)
end_date = pd.to_datetime(end)
result = pd.date_range(start=start_date, end=end_date, periods=n)
print(result)

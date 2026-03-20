    df['datetime'] = df['datetime'].dt.tz_localize(None)
    return df

print(f())

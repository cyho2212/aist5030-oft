result = df.groupby('l')['v'].apply(lambda x: np.nansum(x) if np.isnan(np.nansum(x)) else np.nansum(x))
print(result)

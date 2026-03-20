df = pd.DataFrame(np.concatenate((lat, lon, val), axis=1), columns=['lat', 'lon', 'val'])
print(df)

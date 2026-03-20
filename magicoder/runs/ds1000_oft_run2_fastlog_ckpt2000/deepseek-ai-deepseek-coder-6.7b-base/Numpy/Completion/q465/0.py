    df = pd.DataFrame(columns=['lat', 'lon', 'val'])
    for i in range(len(lat)):
        for j in range(len(lat[0])):
            df = df.append({'lat': lat[i][j], 'lon': lon[i][j], 'val': val[i][j]}, ignore_index=True)
    return df

print(f())

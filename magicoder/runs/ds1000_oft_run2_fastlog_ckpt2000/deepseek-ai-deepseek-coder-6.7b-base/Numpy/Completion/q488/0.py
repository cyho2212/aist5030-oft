scaler = MinMaxScaler()
result = scaler.fit_transform(a.reshape(-1, a.shape[-1])).reshape(a.shape)
print(result)

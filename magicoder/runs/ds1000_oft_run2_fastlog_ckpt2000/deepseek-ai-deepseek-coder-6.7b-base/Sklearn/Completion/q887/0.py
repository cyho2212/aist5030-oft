from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
centered_scaled_data = scaler.fit_transform(data)

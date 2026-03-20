    # Run regression model
    # Check score
    # Inverse the StandardScaler to get back the real time
    inverse_scaled = scaler.inverse_transform(scaled)
    return inverse_scaled

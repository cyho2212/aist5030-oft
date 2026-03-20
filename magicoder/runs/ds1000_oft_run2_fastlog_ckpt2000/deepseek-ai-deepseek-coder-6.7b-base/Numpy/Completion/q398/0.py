B = A * a + B.shift(1) * b
B.iloc[0] = A.iloc[0] * a

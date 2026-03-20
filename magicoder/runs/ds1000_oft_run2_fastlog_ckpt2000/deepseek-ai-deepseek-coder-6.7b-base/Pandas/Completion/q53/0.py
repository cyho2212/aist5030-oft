import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

result = df.copy()
for col in df.columns:
    result[f'sigmoid_{col}'] = sigmoid(df[col])

print(result)

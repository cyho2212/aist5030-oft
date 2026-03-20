B = pd.Series(np.zeros(len(A)))
B[0] = a*A[0]
for i in range(1, len(A)):
    B[i] = a*A[i] + b*B[i-1] + c*B[i-2]
print(B)

result = tf.einsum('bij,bjk->bik', A, B)

# Check the shape
print(result.shape)

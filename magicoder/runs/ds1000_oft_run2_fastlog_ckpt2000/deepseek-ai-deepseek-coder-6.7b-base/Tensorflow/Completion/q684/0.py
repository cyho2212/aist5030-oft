result = tf.expand_dims(a, axis=0)
result = tf.expand_dims(result, axis=-1)

print(result.shape)

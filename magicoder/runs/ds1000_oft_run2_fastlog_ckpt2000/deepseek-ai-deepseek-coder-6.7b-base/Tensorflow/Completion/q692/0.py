result = tf.gather_nd(x, tf.stack([row, col], axis=1))

print(result)

result = tf.gather_nd(x, tf.stack([y, z], axis=1))

print(result)

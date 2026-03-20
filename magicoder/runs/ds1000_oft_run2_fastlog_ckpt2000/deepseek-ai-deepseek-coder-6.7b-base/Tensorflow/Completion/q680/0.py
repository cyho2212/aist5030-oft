result = tf.reshape(tf.stack(tf.meshgrid(a, b), axis=-1), (-1, 2))

print(result)

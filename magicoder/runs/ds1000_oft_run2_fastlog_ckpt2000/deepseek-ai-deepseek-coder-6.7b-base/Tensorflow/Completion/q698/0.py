result = tf.math.divide(tf.reduce_sum(x, axis=-1), tf.reduce_sum(tf.cast(x != 0, tf.float32), axis=-1))
print(result)

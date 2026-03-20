    non_zero_mask = tf.math.count_nonzero(x, axis=-1)
    non_zero_mask = tf.cast(non_zero_mask, tf.float32)
    non_zero_mask = tf.expand_dims(non_zero_mask, axis=-1)
    x = tf.math.divide(x, non_zero_mask)
    x = tf.math.reduce_sum(x, axis=-2)
    return x

print(f())

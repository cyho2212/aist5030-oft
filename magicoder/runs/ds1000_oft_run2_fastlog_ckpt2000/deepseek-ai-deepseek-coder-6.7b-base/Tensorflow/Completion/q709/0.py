    tf.random.set_seed(seed_x)
    return tf.random.uniform(shape=(10,), minval=1, maxval=5, dtype=tf.int32)

print(f())

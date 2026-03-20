    a_shape = tf.shape(a)
    b_shape = tf.shape(b)
    a_indices = tf.reshape(tf.range(a_shape[0]), [a_shape[0], 1])
    b_indices = tf.reshape(tf.range(b_shape[0]), [1, b_shape[0]])
    a_indices = tf.tile(a_indices, [1, b_shape[0]])
    b_indices = tf.tile(b_indices, [a_shape[0], 1])
    a_indices = tf.reshape(a_indices, [-1])
    b_indices = tf.reshape(b_indices, [-1])
    a_values = tf.reshape(a, [-1])
    b_values = tf.reshape(b, [-1])
    return tf.data.Dataset.from_tensor_slices((a_indices, b_indices, a_values, b_values))

for a, b, a_val, b_val in f().as_numpy_iterator():
    print(a, b, a_val, b_val)

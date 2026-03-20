    max_length = tf.reduce_max(lengths)
    mask = tf.sequence_mask(lengths, max_length)
    return mask

print(f())

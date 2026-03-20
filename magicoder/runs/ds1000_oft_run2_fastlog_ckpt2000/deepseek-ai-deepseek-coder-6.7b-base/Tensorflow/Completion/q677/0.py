result = tf.pad(tf.sequence_mask(lengths, maxlen=8), [[0, 0], [0, 0], [0, 4]])

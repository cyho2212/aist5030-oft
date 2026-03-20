    return [input[0]+1, input[0]+2, input[1]+1, input[1]+2, input[2]+1, input[2]+2]

ds = tf.data.Dataset.from_tensor_slices(example_input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(f(x)))

element = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
result = []
with tf.compat.v1.Session() as sess:
    for _ in range(6):
        result.append(sess.run(element))
print(result)

tf_idf_out = pipe.named_steps["tf_idf"].fit_transform(data.test)

# nmf_in = ... # put solution in this variable
# Solution
nmf_in = tf_idf_out

print(tf_idf_out)
print(nmf_in)

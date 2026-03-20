select_out = pipe.named_steps['select'].fit_transform(data, target)

# Print the output
print(select_out)

bin_data = np.array_split(data, len(data) // bin_size)
bin_data_max = np.array([np.max(x) for x in bin_data])
print(bin_data_max)

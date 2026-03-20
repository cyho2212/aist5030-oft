bin_data = np.array([np.array_split(row, len(row)//bin_size) for row in data])
bin_data_mean = np.mean(bin_data, axis=2)
print(bin_data_mean)

bin_data = [np.array_split(row, len(row)//bin_size) for row in data]
bin_data_mean = [np.mean(row, axis=1) for row in bin_data]
print(bin_data)
print(bin_data_mean)

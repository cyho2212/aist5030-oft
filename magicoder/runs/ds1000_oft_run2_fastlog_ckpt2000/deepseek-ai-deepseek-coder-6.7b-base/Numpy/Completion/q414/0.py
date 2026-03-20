bin_data = np.array_split(data, len(data)//bin_size)
bin_data_mean = [np.mean(i) for i in bin_data]
print(bin_data_mean)

bin_data = [data[i:i+bin_size] for i in range(len(data)-bin_size+1)]
bin_data_mean = [np.mean(b) for b in bin_data]
print(bin_data)
print(bin_data_mean)

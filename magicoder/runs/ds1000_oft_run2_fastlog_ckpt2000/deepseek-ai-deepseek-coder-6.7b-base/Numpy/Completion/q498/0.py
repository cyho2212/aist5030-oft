    # Create a new array with the desired shape
    new_arr = np.zeros(shape)
    # Copy the original array into the new array
    new_arr[:arr.shape[0], :arr.shape[1]] = arr
    return new_arr

print(f())

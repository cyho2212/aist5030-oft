    # Convert the softmax output to numpy array
    softmax_output = softmax_output.detach().numpy()
    # Find the index of the maximum value in each row
    max_index = np.argmax(softmax_output, axis=1)
    # Convert the numpy array to torch tensor
    max_index = torch.from_numpy(max_index)
    return max_index

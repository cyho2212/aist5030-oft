result = np.array([np.unpackbits(np.uint8(i))[-m:] for i in a])
print(result)

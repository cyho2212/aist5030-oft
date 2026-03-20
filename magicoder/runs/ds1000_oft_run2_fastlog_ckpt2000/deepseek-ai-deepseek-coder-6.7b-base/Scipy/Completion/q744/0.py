
# Erode the image
eroded = scipy.ndimage.morphology.binary_erosion(square)

# Dilate the image
dilated = scipy.ndimage.morphology.binary_dilation(eroded)

# Subtract the dilated image from the original image
result = square - dilated

# Set all values that are not 0 to 0
result[result != 0] = 1

# Print the result
print(result)

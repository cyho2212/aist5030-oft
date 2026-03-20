square = scipy.ndimage.grey_erosion(square, size=(3, 3))
square = scipy.ndimage.grey_dilation(square, size=(3, 3))

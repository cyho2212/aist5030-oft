    img_thresholded = img > threshold
    labeled_array, num_features = ndimage.label(img_thresholded)
    return num_features

print(f())

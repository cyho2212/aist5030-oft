result = ndimage.label(img > threshold)[0]
print(result)

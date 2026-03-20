    mid = np.array([shape[0]/2, shape[1]/2])
    y, x = np.mgrid[0:shape[0], 0:shape[1]]
    return distance.cdist(np.dstack((y, x)), np.dstack((mid, mid)))

print(f())

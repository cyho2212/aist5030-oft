def cost(x):
    return np.sum(np.abs(points1[x.astype(int)] - points2[x.astype(int)]))

result = scipy.optimize.linear_sum_assignment(scipy.spatial.distance.cdist(points1, points2, 'cityblock'))[1]
print(result)

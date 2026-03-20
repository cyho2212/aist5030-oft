def cost(x):
    return scipy.spatial.distance.cdist(points1[x.astype(int)], points2[x.astype(int)]).sum()

result = scipy.optimize.linear_sum_assignment(scipy.spatial.distance.cdist(points1, points2))[1]
print(result)

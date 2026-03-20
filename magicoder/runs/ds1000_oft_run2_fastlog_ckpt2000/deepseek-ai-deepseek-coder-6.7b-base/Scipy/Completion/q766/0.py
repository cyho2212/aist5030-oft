result = []
for point in extraPoints:
    region = vor.point_region[vor.find_simplex(point)]
    result.append(region)
print(result)

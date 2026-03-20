def smoothclamp(x, x_min, x_max):
    if x < x_min:
        return x_min
    elif x > x_max:
        return x_max
    else:
        return x

# Test the function
print(smoothclamp(x, x_min, x_max))

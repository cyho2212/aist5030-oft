def smoothclamp(x, x_min, x_max, N):
    # Calculate the smoothstep function
    t = np.clip((x - x_min) / (x_max - x_min), 0, 1)
    t = t ** N
    return t * (x_max - x_min) + x_min

# Test the function
print(smoothclamp(x, x_min, x_max, N))

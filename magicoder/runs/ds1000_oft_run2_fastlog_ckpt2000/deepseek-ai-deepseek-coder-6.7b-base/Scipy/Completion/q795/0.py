    return 2*c*x*(high-low)

# Define the range of c
c_range = [1, 2, 3, 4, 5]

# Define the limits of integration
low = 0
high = 1

# Initialize the array to store the results
I = []

# Loop over the range of c
for c in c_range:
    # Integrate the function
    result, error = scipy.integrate.quad(lambda x: f(c, low, high), low, high)
    # Append the result to the array
    I.append(result)

# Print the results
print(I)

import numpy as np

# random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Identify the maximum values along each row
max_values = np.max(reshaped_array, axis=1, keepdims=True)

# Replace the max in each row by 0
reshaped_array[reshaped_array == max_values] = 0

print("Original Array:")
print(random_vector)

print("\nReshaped Array (4 by 5):")
print(reshaped_array)
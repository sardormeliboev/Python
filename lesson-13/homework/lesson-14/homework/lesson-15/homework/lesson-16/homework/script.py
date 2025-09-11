import numpy as np

print("✅ 1. Convert List to 1D Array")
my_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(my_list)
print("Original List:", my_list)
print("One-dimensional NumPy array:", array_1d)
print("-" * 50)

print("✅ 2. Create 3x3 Matrix (2 to 10)")
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3)
print("-" * 50)

print("✅ 3. Null Vector (10) & Update Sixth Value")
null_vector = np.zeros(10)
print("Old vector:", null_vector)
null_vector[6] = 11
print("Updated vector:", null_vector)
print("-" * 50)

print("✅ 4. Array from 12 to 38")
arr_12_38 = np.arange(12, 38)
print(arr_12_38)
print("-" * 50)

print("✅ 5. Convert Array to Float Type")
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("Original array:", arr_int)
print("Float array:", arr_float)
print("-" * 50)

print("✅ 6. Celsius to Fahrenheit Conversion")
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9 / 5 + 32
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("-" * 50)

print("✅ 7. Append Values to Array")
original_array = np.array([10, 20, 30])
appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("Original array:", original_array)
print("Appended array:", appended_array)
print("-" * 50)

print("✅ 8. Array Statistical Functions")
random_array = np.random.rand(10)
print("Random array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))
print("-" * 50)

print("✅ 9. Find Min and Max in 10x10 Array")
array_10x10 = np.random.rand(10, 10)
print("10x10 array:\n", array_10x10)
print("Minimum value:", np.min(array_10x10))
print("Maximum value:", np.max(array_10x10))
print("-" * 50)

print("✅ 10. Create 3x3x3 Array with Random Values")
array_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 random array:\n", array_3x3x3)
print("-" * 50)

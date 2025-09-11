
import numpy as np

#1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

#2. Create 3x3 Matrix (2 → 10)
arr = np.arange(2, 11).reshape(3, 3)
print(arr)

#3. Null Vector (10) & Update Sixth Value
arr = np.zeros(10)
print("Original Null Vector:")
print(arr)

arr[6] = 11   # 6-indeks degani 7-element
print("\nAfter updating sixth value:")
print(arr)

#4. Array from 12 to 38
arr = np.arange(12, 38)
print(arr)

#5. Convert Array to Float Type
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array converted to float:", float_arr)

#6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32

print("Values in Celsius degrees:")
print(celsius)

print("\nValues in Fahrenheit degrees:")
print(fahrenheit)

#7. Append Values to Array
arr = np.array([10, 20, 30])
print("Original array:", arr)

arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append:", arr)

#8. Array Statistical Functions
arr = np.random.randint(1, 100, 10)
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

#9. Find Min and Max in 10x10 Array
arr = np.random.rand(10, 10)
print("Array:\n", arr)

print("\nMinimum value:", arr.min())
print("Maximum value:", arr.max())

#10. Create 3x3x3 Array with Random Values
arr = np.random.rand(3, 3, 3)
print("3x3x3 Array:\n", arr)

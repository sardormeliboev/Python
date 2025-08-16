# 1. Create and Access List Elements
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Third fruit:", fruits[2])  # Index 2 = 3rd element
# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("Concatenated List:", concatenated)
# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
middle_index = len(numbers) // 2
extracted = [numbers[0], numbers[middle_index], numbers[-1]]
print("Extracted Elements:", extracted)
# 4. Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "The Matrix", "Interstellar"]
movies_tuple = tuple(movies)
print("Movies Tuple:", movies_tuple)
# 5. Check Element in a List
cities = ["London", "New York", "Paris", "Tokyo"]
print("Is Paris in the list?", "Paris" in cities)
# 6. Duplicate a List Without Using Loops
nums = [1, 2, 3]
duplicated = nums * 2
print("Duplicated List:", duplicated)
# 7. Swap First and Last Elements of a List
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("Swapped List:", nums)
# 8. Slice a Tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice from index 3 to 7:", tup[3:8])
# 9. Count Occurrences in a List
colors = ["blue", "red", "blue", "green", "blue"]
print("Blue appears:", colors.count("blue"), "times")
# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))
# 11. Merge Two Tuples
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
merged_tuple = tup1 + tup2
print("Merged Tuple:", merged_tuple)
# 12. Find the Length of a List and Tuple
sample_list = [1, 2, 3, 4]
sample_tuple = (10, 20, 30)
print("List length:", len(sample_list))
print("Tuple length:", len(sample_tuple
# 13. Convert Tuple to List
tup_nums = (5, 10, 15, 20, 25)
list_nums = list(tup_nums)
print("Converted List:", list_nums)
# 14. Find Maximum and Minimum in a Tuple
tup_vals = (100, 50, 200, 25, 75)
print("Max value:", max(tup_vals))
print("Min value:", min(tup_vals))
# 15. Reverse a Tuple
words = ("one", "two", "three")
reversed_tuple = words[::-1]
print("Reversed Tuple:", reversed_tuple)
         

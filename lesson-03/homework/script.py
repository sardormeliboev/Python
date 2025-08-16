fruits = ["apple", "banana", "pear", "peach", "orange"]
print("Third fruit:", fruits[2])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
umumiy_list = list1 + list2
print("umumiy_list_1_2:", umumiy_list)

numbers = [1, 2, 3, 4, 5]
middle_index = len(numbers) // 2
list = [numbers[0], numbers[middle_index], numbers[-1]]
print("yangi ruyxat:", list)

movies = ["Ipman", "Titanic", "Avatar", "Yulduzlar jangi", "Kalmar"]
movies_tuple = tuple(movies)
print("Movies Tuple:", movies_tuple)

cities = ["London", "New York", "Paris", "German", "Sidney"]
print("Is Paris in the list?", "Paris" in cities)

nums = [1, 2, 3]
duplicat = nums * 2
print("Duplicat List:", duplicat)

nums = [1, 2, 3, 4, 5]
nums[0], nums[-1] = nums[-1], nums[0]
print("New List:", nums)

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Chop et from index 3 to 7:", tup[3:8])

colors = ["blue", "red", "blue", "green", "blue"]
print("kuk takrorlandi:", colors.count("blue"), "marta")

animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
merged_tuple = tup1 + tup2
print("Merged Tuple:", merged_tuple)

list = [1, 2, 3, 4]
tuple = (10, 20, 30)
print("List length:", len(list))
print("Tuple length:", len(tuple))

tup_nums = (5, 10, 15, 20, 25)
list_nums = list(tup_nums)
print("ruyxat:", list_nums)

tup_vals = (100, 50, 200, 25, 75)
print("Max value:", max(tup_vals))
print("Min value:", min(tup_vals))

words = ("one", "two", "three")
reversed_tuple = words[::-1]
print("Reversed Tuple:", reversed_tuple)

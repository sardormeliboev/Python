# Sample dictionary
my_dict = {1: 2, 3: 1, 2: 3}

# Sort ascending
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc)

# Sort descending
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30  # Yangi key va value qo‘shish
print(sample_dict)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Yangi dictionary yaratish
merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

print(merged_dict)

n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)

squares_15 = {x: x**2 for x in range(1, 16)}
print(squares_15)

# 1. Create a Set
my_set = {1, 2, 3}
print("Created Set:", my_set)

# 2. Iterate Over a Set
print("Iterating Set:")
for item in my_set:
    print(item)

# 3. Add Member(s) to a Set
my_set.add(4)           # Add single item
my_set.update([5, 6])   # Add multiple items
print("After Adding:", my_set)

# 4. Remove Item(s) from a Set
my_set.remove(6)  # Removes 6, will error if not found
print("After Remove:", my_set)

# 5. Remove an Item if Present in the Set
my_set.discard(10)  # Does nothing if item not found
print("After Discard:", my_set)

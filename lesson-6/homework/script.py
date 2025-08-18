# ------------------------
# 1. Modify String with Underscores
# ------------------------
def insert_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0

    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3 and i != len(txt) - 1:
            if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == "_"):
                pass
            else:
                result += "_"
            count = 0
        i += 1
    return result

# Test
print(insert_underscores("hello"))        # hel_lo
print(insert_underscores("assalom"))      # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))


# ------------------------
# 2. Integer Squares Exercise
# ------------------------
def integer_squares(n):
    for i in range(n):
        print(i**2)

# Example
integer_squares(5)


# ------------------------
# 3. Loop-Based Exercises
# ------------------------

# 3.1 First 10 natural numbers
print("\nFirst 10 natural numbers:")
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2 Number pattern
print("\nNumber pattern:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 3.3 Sum of numbers
num = 10
total = 0
for i in range(1, num+1):
    total += i
print("\nSum is:", total)

# 3.4 Multiplication table
print("\nMultiplication table:")
n = 2
for i in range(1, 11):
    print(n * i)

# 3.5 Filter numbers from list
print("\nFiltered numbers:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num <= 150:
        print(num)

# 3.6 Count digits
num = 75869
print("\nTotal digits:", len(str(num)))

# 3.7 Reverse number pattern
print("\nReverse number pattern:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# 3.8 Print list in reverse
print("\nList in reverse:")
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# 3.9 Numbers -10 to -1
print("\nNumbers -10 to -1:")
for i in range(-10, 0):
    print(i)

# 3.10 Done after loop
print("\nLoop with Done:")
for i in range(5):
    print(i)
print("Done!")

# 3.11 Prime numbers in range
print("\nPrime numbers between 25 and 50:")
start, end = 25, 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# 3.12 Fibonacci series
print("\nFibonacci sequence:")
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end="  ")
    a, b = b, a+b
print()

# 3.13 Factorial
print("\nFactorial:")
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"{num}! = {fact}")


# ------------------------
# 4. Return Uncommon Elements of Lists
# ------------------------
def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result

# Tests
print("\nUncommon elements:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))

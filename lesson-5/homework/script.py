yil = int(input("Yilni kiriting:"))
if (yil % 400 == 0) or (yil % 4 == 0 and yil % 100 != 0):
    print("Kabisa yil (366 kun, fevral 29).")
else:
    print("Oddiy yil (365 kun)")

n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

a = int(input("a: "))
b = int(input("b: "))

start = a if a % 2 == 0 else a + 1
end = b if b % 2 == 0 else b - 1

if start > end:
    print([])  # juft son yo'q
else:
    evens = list(range(start, end + 1, 2))
    print(evens)

a = int(input("a: "))
b = int(input("b: "))

evens = list(range(a + (a % 2), b + 1 - (b % 2), 2))
print(evens)

# 1. ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
#2. ValueError
try:
    n = int(input("Butun son kiriting: "))
except ValueError:
    print("Bu butun son emas!")

#3. FileNotFoundError
3. FileNotFoundError
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi!")

#4. TypeError
try:
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    print(a + b)
except TypeError:
    print("Faqat son kiritish mumkin!")
  #5. PermissionError
try:
    with open("/etc/passwd", "w") as f:
        f.write("test")
except PermissionError:
    print("Ruxsat yo‘q!")
  #6. IndexError
try:
    arr = [1, 2, 3]
    print(arr[5])
except IndexError:
    print("Bunday indeks yo‘q!")

#7. KeyboardInterrupt
try:
    n = input("Son kiriting: ")
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi.")

#8. ArithmeticError
try:
    x = 1 / 0
except ArithmeticError:
    print("Arifmetik xatolik yuz berdi!")

#9. UnicodeDecodeError

try:
    with open("test.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Kodlashda xatolik!")

#10. AttributeError

try:
    x = [1, 2, 3]
    x.upper()
except AttributeError:
    print("Bunday atribut mavjud emas!")

#Python File Input Output: Exercises, Practice, Solution

#1. Faylni o‘qish
with open("sample.txt", "r") as f:
    print(f.read())

#2. Faylning dastlabki n qatorini o‘qish
n = 3with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)

with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

#3.Faylga qo‘shib yozish (append) va o‘qish
with open("sample.txt", "a") as f:
    f.write("\nYangi qator qo‘shildi.")

with open("sample.txt", "r") as f:
    print(f.read())

#4. Faylning oxirgi n qatorini o‘qish
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line, end="")
      

#5. Faylni qatorma-qator o‘qib, listga saqlash
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)

#6. Faylni qatorma-qator o‘qib, bitta stringga saqlash
with open("sample.txt", "r") as f:
    text = f.read()
print(text)

#7. Fayldan arrayga (listga) o‘qib olish
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)

#8. Fayldagi eng uzun so‘z(lar)ni topish
with open("sample.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Eng uzun so‘z:", longest)

#9. Fayldagi qatorlar sonini hisoblash
with open("sample.txt", "r") as f:
    lines = f.readlines()
print("Qatorlar soni:", len(lines))

#10. Fayldagi so‘zlar chastotasini hisoblash
from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().split()

freq = Counter(words)
print(freq)

#11. Fayl hajmini aniqlash (baytlarda)
import os

size = os.path.getsize("sample.txt")
print("Fayl hajmi:", size, "bayt")

#12. Listni faylga yozish
data = ["apple", "banana", "cherry"]

with open("list.txt", "w") as f:
    for item in data:
        f.write(item + "\n")

#13. Faylni boshqa faylga nusxalash
with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)

#14. Ikki fayldagi mos qatorlarni birlashtirish
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

#15. Tasodifiy qatorni o‘qish
import random

with open("sample.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))

#16. Fayl yopilganmi yoki yo‘qmi tekshirish
f = open("sample.txt", "r")
print("Yopilganmi?", f.closed)
f.close()
print("Yopilganmi?", f.closed)

#17. Fayldan \n belgilarini olib tashlash
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)

#18. Fayldagi so‘zlar sonini hisoblash
with open("sample.txt", "r") as f:
    text = f.read().replace(",", " ")
    words = text.split()
print("So‘zlar soni:", len(words))

#19. Bir nechta fayllardan belgilarni yig‘ib olish
files = ["sample.txt", "copy.txt"]
chars = []

for file in files:
    with open(file, "r") as f:
        chars.extend(list(f.read()))

print(chars[:50])  # faqat bir qismini chiqarish

#20. A.txt dan Z.txt gacha fayllar yaratish
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is {letter}.txt file.\n")

#21. Fayl yaratib, alifboni bo‘lib yozish
import string

letters = string.ascii_uppercase
n = 5  # har qatorda nechta harf bo‘lishi kerak

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(" ".join(letters[i:i+n]) + "\n")





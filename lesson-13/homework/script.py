#1. Age Calculator (Tug‘ilgan sanadan yosh hisoblash)
from datetime import datetime

birth_date = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD): ")
birth = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.today()

years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day

if days < 0:
    months -= 1
    days += 30
if months < 0:
    years -= 1
    months += 12

print(f"Sizning yoshingiz: {years} yil, {months} oy, {days} kun.")

#2. Days Until Next Birthday (Keyingi tug‘ilgan kungacha qolgan kunlar)
from datetime import datetime, timedelta

birth_date = input("Tug'ilgan kuningiz (YYYY-MM-DD): ")
birth = datetime.strptime(birth_date, "%Y-%m-%d")
today = datetime.today()

next_birthday = birth.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"Keyingi tug'ilgan kuningizgacha {days_left} kun qoldi.")

#3. Meeting Scheduler (Uchrashuv tugash vaqtini hisoblash)
from datetime import datetime, timedelta

now = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

start_time = datetime.strptime(now, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print("Uchrashuv tugash vaqti:", end_time.strftime("%Y-%m-%d %H:%M"))

#4. Timezone Converter (Vaqt zonasi o‘zgartirgich)
from datetime import datetime
import pytz

dt_str = input("Vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_zone = input("Hozirgi timezone (masalan, Asia/Tashkent): ")
to_zone = input("O'zgartirmoqchi bo'lgan timezone (masalan, US/Eastern): ")

naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

local_dt = from_tz.localize(naive_dt)
converted = local_dt.astimezone(to_tz)

print("O'zgartirilgan vaqt:", converted.strftime("%Y-%m-%d %H:%M"))

#5. Countdown Timer (Orqaga sanovchi taymer)
import time
from datetime import datetime

target_str = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if target <= now:
        print("Vaqt tugadi!")
        break
    diff = target - now
    print("Qolgan vaqt:", diff, end='\r')
    time.sleep(1)

  #6. Email Validator (Email manzilni tekshiruvchi)
  import re

email = input("Email manzilni kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Email manzil to‘g‘ri.")
else:
    print("Noto‘g‘ri email manzil.")

#7. Phone Number Formatter (Telefon raqamni formatlash)
number = input("Telefon raqamni kiriting (faqat raqamlar): ")

if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatlangan:", formatted)
else:
    print("Noto‘g‘ri raqam.")

#8. Password Strength Checker (Parol kuchini tekshirish)
import re

password = input("Parolni kiriting: ")

length = len(password) >= 8
upper = re.search(r'[A-Z]', password)
lower = re.search(r'[a-z]', password)
digit = re.search(r'\d', password)

if length and upper and lower and digit:
    print("Parol kuchli.")
else:
    print("Parol zaif. Kamida 8ta belgi, 1ta katta harf, kichik harf va raqam bo‘lishi kerak.")

#9. Word Finder (Matndan so‘z topuvchi)
text = """Python is great. Python is easy to learn. Many people love Python."""
word = input("Qidirilayotgan so‘z: ")

count = text.lower().count(word.lower())
print(f'"{word}" so‘zi {count} marta topildi.')

#10. Date Extractor (Matndan sanalarni ajratib olish)
import re

text = input("Matnni kiriting: ")

# Sana formatlari: YYYY-MM-DD, DD/MM/YYYY, etc.
pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b'

dates = re.findall(pattern, text)

if dates:
    print("Topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("Hech qanday sana topilmadi.")

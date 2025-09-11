#1. JSON Parsing – students.json faylini o'qish
import json

# students.json faylini ochamiz va ma'lumotlarni o'qib chiqamiz
with open('students.json', 'r') as file:
    students = json.load(file)

# Har bir talabani chiqaramiz
for student in students:
    print("Ism:", student.get('name'))
    print("Yosh:", student.get('age'))
    print("Kurs:", student.get('course'))
    print("----------------------")
#students.json fayl quyidagicha ko'rinishda bo'lishi kerak:
[
    {"name": "Ali", "age": 20, "course": "Matematika"},
    {"name": "Laylo", "age": 22, "course": "Ingliz tili"}
]

#2. Weather API – Tashkent ob-havosini olish
import requests

# OpenWeather saytidan API kalitingiz kerak bo'ladi
API_KEY = 'YOUR_API_KEY'  # bu yerga o'zingizning API kalitingizni yozing
CITY = 'Tashkent'

url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(url)
data = response.json()

# Ob-havo ma'lumotlarini chiqarish
print("Shahar:", CITY)
print("Temperatura:", data['main']['temp'], "°C")
print("Namlik:", data['main']['humidity'], "%")
print("Tavsif:", data['weather'][0]['description'])

#3. JSON Modification – books.json faylini boshqarish
import json

# Faylni o'qish funksiyasi
def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Faylga yozish funksiyasi
def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

# Kitob qo'shish
def add_book():
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Kitob qo‘shildi!")

# Kitob yangilash
def update_book():
    title = input("Qaysi kitobni yangilamoqchisiz? ")
    books = load_books()
    for book in books:
        if book["title"] == title:
            book["author"] = input("Yangi muallif: ")
            save_books(books)
            print("Yangilandi!")
            return
    print("Kitob topilmadi.")

# Kitob o‘chirish
def delete_book():
    title = input("Qaysi kitobni o‘chirmoqchisiz? ")
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print("Kitob o‘chirildi!")

# Menyu
while True:
    print("\n1. Qo‘shish\n2. Yangilash\n3. O‘chirish\n4. Chiqish")
    choice = input("Tanlang: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        break
    else:
        print("Noto‘g‘ri tanlov.")

#4. Movie Recommendation System – Janr bo‘yicha film tavsiyasi
import requests
import random

API_KEY = 'YOUR_API_KEY'  # OMDb API kalitingizni yozing

def recommend_movie(genre):
    # OMDb API janrga qarab izlash uchun filter yo'q, shuning uchun random filmlar ichidan tanlaymiz
    movie_list = ["Inception", "Titanic", "Avatar", "Gladiator", "Interstellar", "The Matrix"]
    
    for movie in random.sample(movie_list, len(movie_list)):
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie}"
        response = requests.get(url)
        data = response.json()
        if genre.lower() in data.get("Genre", "").lower():
            print("Tavsiya etilgan film:")
            print("Nomi:", data["Title"])
            print("Janr:", data["Genre"])
            print("IMDB bahosi:", data["imdbRating"])
            print("Yil:", data["Year"])
            return

    print("Uzr, bu janrda film topilmadi.")

# Foydalanuvchidan janr so‘raymiz
user_genre = input("Qaysi janrda film tomosha qilmoqchisiz? (Masalan: Action, Drama, Sci-Fi): ")
recommend_movie(user_genre)

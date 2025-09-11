
import pandas as pd
import numpy as np   # random sonlar uchun
#Homework 3
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# 1. Ustun nomlarini o'zgartirish
df.rename(columns={"First Name": "first_name", "Age": "age"}, inplace=True)

# 2. Birinchi 3 qator
print("First 3 rows:")
print(df.head(3))

# 3. O'rtacha yosh
print("\nMean age:", df['age'].mean())

# 4. Faqat ism va shahar ustunlari
print("\nName and City columns:")
print(df[['first_name', 'City']])

# 5. Yangi 'Salary' ustuni qo'shish
df['Salary'] = np.random.randint(4000, 8000, size=len(df))
print("\nDataFrame with Salary:")
print(df)

# 6. Statistik ma'lumotlar
print("\nSummary statistics:")
print(df.describe())

#Homework 2
import pandas as pd

# 1. DataFrame yaratish
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [5000, 6000, 7500, 8000],
        'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)

print("Sales and Expenses DataFrame:")
print(sales_and_expenses)

# 2. Maksimum qiymatlar
print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

# 3. Minimum qiymatlar
print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

# 4. O'rtacha qiymatlar
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

#Homework 3
import pandas as pd

# 1. DataFrame yaratish
data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'January': [1200, 200, 300, 150],
        'February': [1300, 220, 320, 160],
        'March': [1400, 240, 330, 170],
        'April': [1500, 250, 350, 180]}

expenses = pd.DataFrame(data)

# Category ustunini index qilish
expenses = expenses.set_index('Category')
print("Expenses DataFrame:")
print(expenses)

# 2. Har bir kategoriya bo‘yicha maksimal xarajat
print("\nMax expense for each category:")
print(expenses.max(axis=1))

# 3. Har bir kategoriya bo‘yicha minimal xarajat
print("\nMin expense for each category:")
print(expenses.min(axis=1))

# 4. Har bir kategoriya bo‘yicha o‘rtacha xarajat
print("\nAverage expense for each category:")
print(expenses.mean(axis=1))


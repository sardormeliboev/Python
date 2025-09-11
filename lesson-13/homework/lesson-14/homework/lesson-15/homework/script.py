import sqlite3

# Baza bilan ulanish
conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()

# 1. Jadval yaratish
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# 2. Ma'lumot qo'shish
cursor.execute("INSERT INTO Roster VALUES ('Benjamin Sisko', 'Human', 40)")
cursor.execute("INSERT INTO Roster VALUES ('Jadzia Dax', 'Trill', 300)")
cursor.execute("INSERT INTO Roster VALUES ('Kira Nerys', 'Bajoran', 29)")

# 3. Yangilash
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# 4. Faqat Bajoranlar
cursor.execute('''
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
''')
results = cursor.fetchall()

print("Bajoranlar:")
for row in results:
    print("Ism:", row[0], "| Yosh:", row[1])

# Baza yopiladi
conn.commit()
conn.close()

txt = 'MsaatmiazD'
txt = txt[0]+txt[2]+txt[4]+txt[6]+txt[8]
txt

txt = 'MsaatmiazD'
txt = txt[9]+txt[7]+txt[5]+txt[3]+txt[1]
txt

txt = "I'm John. I am from London"
country = txt.split()
country[-1]

txt = 'Uzbekistan'
txt[::-1]

txt = 'fantan'
txt == txt[::-1]

txt = ['olma', 'uzum', 'banan', 'nok', 'shaftoli']
txt[2]

ls = [1,2,3,4]
ls1 = [5,6,7,8]
ls.extend(ls1)
ls

ls = [1, 2, 3, 4, 5, 6, 7]
ls1 = [ls[0], ls[3], ls[-1]]
print(ls1)

country = ["London", "Paris", "Berlin"]
if "Paris" in country:
    print("Paris ro'yxatda bor")
else:
    print("Paris ro'yxatda yo'q")

ls = [1,2,3,4]
yangi = ls*2
print(yangi)

ls = [1,2,3,4]
ls[0],ls[-1] = ls[-1],ls[0]
print(ls)

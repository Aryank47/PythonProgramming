a = ['raj', 55, 34, 'Mohan', "Aryan"]
b=a.copy()
print(b)
for i in b:
    print(i)

a.insert(2,"hi")
print(a)

a.append("hello")
print(a)

a.clear()
print(a)
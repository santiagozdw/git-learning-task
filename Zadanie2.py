print("Zadanie2")
a = []
cubed = []
squared = []
for i in range(100):
    if i % 5 == 0:
        a.append(i)
cubed = [number * number * number for  number in a]
squared = [number * number for  number in a]
print(a)
print(squared)
print(cubed)

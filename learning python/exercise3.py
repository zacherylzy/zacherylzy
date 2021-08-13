"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print (x)
"""

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for x in a:
    if x < 5:
        b.append(x)

print(b)
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

number = int(input("give me a number please "))

for x in a:
    if number > x:
        b.append(x)
print (b)

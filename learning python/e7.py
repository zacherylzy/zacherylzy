a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = []

for i in a:
    if i%2 == 0:
        b.append(i)

print(b)



"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]

print (b)
"""


"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = []

c = []

for x in a:
    if x % 2 == 0:
        b.append(x)
    else:
        c.append(x)

print (c)
"""

"""
a = [2,3,5,6,7,41,3243,433]
b = [5,2,3,6]

intersects = []

for x in a:
    if x in b:
        intersects.append(x)

print(intersects)
"""

#the better way#
a = [2,3,5,6,7,41,3243,433]
b = [5,2,3,6]


"""
print(returnMatches(a, b))
(doesnt work for some reason)
or

print(set(a) & set(b))

or

print(set(a).intersection(b))
"""

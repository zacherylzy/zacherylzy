number = int(input("Give me a number. I will list all of its divisors "))

divisor = list(range (1, 9999))
#list (range(x) is the same as range(x) for this question.
#be careful when there's a zero in the answer, it may fail the entire code

success = []

for x in divisor:
    if number % x == 0:
        success.append(x)

print(success)


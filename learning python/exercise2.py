
number = int(input("Give me a number "))
checker = int(input("Give me a number to divide the previous number by "))

if number%2 == 0:
    if number%checker == 0:
        print("your first number is even and is divisible by the second number")
    elif number%4 == 0:
        print ("your first number is even, not divisible by the second number, and is a multiple of 4")
    else:
        print("your first number is even but is not divisible by the second number and is not a multiple of 4")

else:
    if number%checker == 0:
        print ('your first number is odd but is divisible by the second number')
    else:
        print ('your first number is odd and is indivisible by the second number')


name = input("give me your name: ")

print('your name is ' + name)

age = input('how old are you? ')

age_left = str(100 - int(age))

print('you will be 100 years old in ' + age_left + ' years')

repeat = input('how many times would you like the previous message repeated? ')

repeat = int(repeat)

print(repeat * age_left)

list = []
i = 0

while i in range(0, 4):
    try:
        if i == 0:
            user_input = float(
                input('Please input the first number: '))  # First Number
            list.append(user_input)

        elif i == 1:
                user_input = float(
                    input('Please input the second number: '))  # Second Number
                list.append(user_input)

        elif i == 2:
                user_input = float(
                    input('Please input the third number: '))  # Third Number
                list.append(user_input)

        elif i == 3:
                user_input = float(
                    input('Please input the fourth number: '))  # Fourth NUmber
                list.append(user_input)
    except ValueError:
        print('Your input is not a number!')
        i = i-1
    i = i+1
list.sort()
print("The second smallest value is", list[1])
print("Program ends.")

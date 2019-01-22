credit_sum = 0
score = 0

while True:
    x = input()
    user_input = x.split()

    if float(user_input[0]) == -1:
        print("Program ends.")
        break
    else:
        if (float(user_input[0]) < 0 or int(user_input[1]) < 0):
            print("Wrong input!")
            x = (input())
            user_input = x.split()
            if float(user_input[0]) == -1:
                print("Program ends.")
                break
    credit_sum = credit_sum + int(user_input[1])
    score = score + float(user_input[0]) * int(user_input[1])
    gpa = score/credit_sum

    print("Current GPA:", "%.2f" % gpa)

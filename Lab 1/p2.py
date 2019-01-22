while True:
    i = 0
    try:
        integer = int(input("Enter an integer: "))
    except ValueError:
        print("Program ends.")
        quit()

    if integer == -1:
        print("Program ends.")
        break
    string = input("Enter a string:")

    while i in range(0, integer):
        print(string*(i+1))
        i = i+1

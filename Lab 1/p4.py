import getpass
ans = int(getpass.getpass("Player 1, write down your number secretly:"))
n = 0

while n < 6:
    guess = int(input("Player 2, input your guess:"))
    n = n + 1

    if (guess < ans and n < 6):
        print("Your guess is too low!")

    else:
        if (guess > ans and n < 6):
            print("Your guess is too high!")

        else:
            if guess == ans:
                print("You are right after trying for",
                      n, "times. Program ends.")
                quit()

print("You have tried 6 times and it is still wrong! The answer is",
      ans, "and program ends.")

userInput = input("Please input a palindrome: ")

while True:
    userInput = userInput.lower()
    reverse = userInput[::-1]
    
    if userInput == reverse:
        print("Welcome to the wonderland!")
        break
    
    else:
        userInput = input("No, you must input a palindrome: ")

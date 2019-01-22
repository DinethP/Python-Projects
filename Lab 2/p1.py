

def roman_number(n):

    if n < 1 or n > 9999:
        value = 'Number is out of range'
        return value

    digit1 = int(n % 10)
    digit2 = int((n/10) % 10)
    digit3 = int((n/100) % 10)
    digit4 = int(n/1000)

    if digit1 in range(0, 4):
        char1 = ("I" * digit1)
    else:
        if digit1 == 4:
            char1 = "IV"
        else:
            if digit1 == 5:
                char1 = "V"
            else:
                if digit1 in range(6, 9):
                    char1 = ("V" + "I" * (digit1 - 5))
                else:
                    if digit1 == 9:
                        char1 = "IX"

    if digit2 in range(0, 4):
        char2 = ("X" * digit2)
    else:
        if digit2 == 4:
            char2 = "XL"
        else:
            if digit2 == 5:
                char2 = "L"
            else:
                if digit2 in range(6, 9):
                    char2 = ("L" + "X" * (digit2 - 5))
                else:
                    if digit2 == 9:
                        char2 = "XC"

    if digit3 in range(0, 4):
        char3 = ("C" * digit3)
    else:
        if digit3 == 4:
            char3 = "CD"
        else:
            if digit3 == 5:
                char3 = "D"
            else:
                if digit3 in range(6, 9):
                    char3 = ("D" + "C" * (digit3 - 5))
                else:
                    if digit3 == 9:
                        char3 = "CM"

    char4 = ("M" * digit4)

    roman_string = char4 + char3 + char2 + char1
    return roman_string

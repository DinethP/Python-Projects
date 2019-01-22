import collections


def count_alphabet(test_string):
    test_string = ''.join(filter(str.isalpha, test_string))
    count = len(test_string)
    return count


def vowel_capitalization(test_string):
    vowels = 'aeiou'
    new_string = ''

    for letter in test_string:
        if letter in vowels:
            letter.upper()
            new_string = new_string + letter.capitalize()
        else:
            new_string = new_string + letter
    return new_string


def concat(test_string, new_string):
    string = test_string + new_string
    return string


def search(test_string, sub):
    return test_string.find(sub)

import collections


def letter_count(string):

    counts = ''.join(filter(str.isalpha, string))
    print(counts)
    counts = collections.Counter(counts.lower()) #collections.Counter returns a dictionary
    print(counts)
    counts = sorted(counts.items()) #.items() returns the key and value
    return counts
print(letter_count('hello my'))
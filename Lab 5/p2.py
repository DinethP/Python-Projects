from functools import reduce

def word_count(x, n, str):
    return reduce(lambda x, y: x + y,
                  map(lambda x: x.count(str),
                      list(filter(lambda string: len(string) > n, x))))

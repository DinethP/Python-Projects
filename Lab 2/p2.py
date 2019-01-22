

def recursive_pow(x, n):
    if n == 0:
        return 1
    else:
        if n > 0:
            return float(x * recursive_pow(x, n-1))

inp = int(input('X value: '))
inp2 = int(input('Enter power: '))
print('Recursive result: '+ "{0:.2}".format(recursive_pow(inp,inp2)))
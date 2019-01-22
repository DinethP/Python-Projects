square_numbers = list(map(lambda x: x*x, [number for number in range(1, 11)]))
subtract_1 = list(map(lambda x: x-1, [number for number in range(1, 11)]))
larger_than_6 = [number for number in range(1, 11) if number >= 6]
power_3_even_numbers = list(
    map(lambda x: x*x*x, [number for number in range(1, 11) if number % 2 == 0]))

print(larger_than_6)
print(power_3_even_numbers)

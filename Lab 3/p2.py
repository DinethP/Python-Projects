def quicksort(a):
    low = []
    high = []
    pivot = []
    ordered_list = []

    if len(a) <= 1:
        return a
    else:
        pivot_value = a[0]

        low = [item for item in a if item < pivot_value]
        high = [item for item in a if item > pivot_value]
        pivot = [item for item in a if item == pivot_value]

    high = quicksort(high)
    low = quicksort(low)

    ordered_list = low + pivot + high
    return ordered_list

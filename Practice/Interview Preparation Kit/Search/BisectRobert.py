def bisect_left(a, b):
    if not a:
        return 0

    low = 0
    high = len(a)
    while low < high:
        middle = (low + high) // 2
        if b <= a[middle]:
            high = middle
        else:
            low = middle + 1
    return low

def bisect_right(a, b):
    if not a:
        return 0

    low = 0
    high = len(a)

    while low < high:
        middle = (low + high) // 2
        if b == a[middle]:
            low = middle
            if low + 1 == len(a) or a[low+1] > a[low]:
                return low + 1
        elif b < a[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return low

def binary_search(l, target, low=None, high=None):
    if high is None:
        high = len(l)-1
    if low is None:
        low = 0
    if low > high:
        return -1

    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    l = [1, 2, 4, 6, 8, 9, 10]
    target = 9

    print(binary_search(l, target))

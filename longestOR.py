def longest_good_subarray(mn, mx, n, arr):
    l = 0
    r = 1
    lor = 0
    while r < len(arr):
        i = l
        tempor = 0
        for i in range(r + 1):
            tempor |= arr[i]
        lor = max(lor, tempor)
        if lor >= mn:
            l += 1
        r += 1
        return r - l


result = longest_good_subarray(1, 2, 5, [0, 3, 4, 1, 5])
print(result)

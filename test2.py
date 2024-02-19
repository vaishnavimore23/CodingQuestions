def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def longest_good_subarray(mn, mx, n, arr):
    max_length = 0
    for i in range(n):
        current_value = 0
        for j in range(i, n):
            current_value |= arr[j]
            num_set_bits = count_set_bits(current_value)
            if mn <= num_set_bits <= mx:
                max_length = max(max_length, j - i + 1)
    return max_length


# Example usage:
mn = 1
mx = 2
n = 5
arr = [0, 3, 4, 1, 5]

result = longest_good_subarray(mn, mx, n, arr)
print(result)  # Output: 3

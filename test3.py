def minimumCycles(arr):
    # Calculate the frequency of each number in the array.
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1

    # The target value is initially set to the maximum value in the array,
    # but we will check if adjusting the target down can reduce operations.
    max_val = max(arr)

    # Minimum operations initialized to a high value.
    min_ops = float("inf")

    # Check each potential target from the minimum value in the array to the maximum.
    for target in range(min(arr), max_val + 1):
        current_ops = 0
        for num, count in freq.items():
            if num > target:
                # If the current number is already larger than the target, it's not feasible.
                current_ops = float("inf")
                break
            diff = target - num
            # Calculate operations based on the difference.
            # If diff is odd: one operation will be +1, the rest will be +2.
            # If diff is even: all operations can be +2.
            if diff % 3 == 0:
                current_ops += (diff // 3) * 2 * count
            else:
                current_ops += ((diff // 3) * 2 + 1) * count

        min_ops = min(min_ops, current_ops)

    return min_ops if min_ops != float("inf") else 0


# Test the function with an example
arr_example = [4, 4, 3, 5, 5]
print(minimumCycles(arr_example))

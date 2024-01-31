def count_occurrences(N, k, x):
    # This function counts how many numbers between 0 and N (inclusive) have the digit x occurring exactly k times

    def has_k_occurrences(number, digit, count):
        # This helper function checks if 'number' contains 'digit' exactly 'count' times
        return str(number).count(str(digit)) == count

    count = 0
    for number in range(N + 1):
        if has_k_occurrences(number, x, k):
            count += 1

    return count


# Example usage
example1 = count_occurrences(11, 1, 1)  # For the first example
example2 = count_occurrences(11, 2, 1)  # For the second example

print("Example 1 Result:", example1)
print("Example 2 Result:", example2)

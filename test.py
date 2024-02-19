def segmentMax(n, q, cat, cnt, l, r):
    result = []

    for i in range(q):
        left = l[i] - 1  # Adjusting to 0-based index
        right = r[i] - 1  # Adjusting to 0-based index

        # Create dictionaries to store maximum count for each category within the range
        max_count = {}

        # Find maximum count for each category within the specified range
        for j in range(left, right + 1):
            category = cat[j]
            count = cnt[j]
            max_count[category] = max(max_count.get(category, 0), count)

        # Sum up the maximum counts for this query
        query_sum = sum(max_count.values())

        # Append the result to the answer array
        result.append(query_sum)

        # Clear the counts in the specified range
        for j in range(left, right + 1):
            cnt[j] = 0

    return result


# Example usage:
n = 5
q = 2
cat = [1, 2, 1, 1, 3]
cnt = [5, 3, 4, 5, 2]
l = [1, 1]
r = [3, 5]

result = segmentMax(n, q, cat, cnt, l, r)
print(result)  # Output: [8, 7]

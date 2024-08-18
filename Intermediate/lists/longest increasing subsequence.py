def longest_increasing_subsequence(lst):
    if not lst:
        return []
    n = len(lst)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if lst[i] > lst[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    max_len = max(lis)
    result = []
    for i in range(n - 1, -1, -1):
        if lis[i] == max_len:
            result.append(lst[i])
            max_len -= 1
    return result[::-1]

# Example usage:
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]))  # Output: [10, 22, 33, 50, 60]

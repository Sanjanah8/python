def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum

# Example usage:
print(cumulative_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]

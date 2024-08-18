def even_odd_difference(lst):
    even_sum = sum(num for num in lst if num % 2 == 0)
    odd_sum = sum(num for num in lst if num % 2 != 0)
    return even_sum - odd_sum

# Example usage:
print(even_odd_difference([1, 2, 3, 4, 5]))  # Output: 2

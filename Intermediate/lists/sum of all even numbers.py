def sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

# Example usage:
print(sum_of_evens([1, 2, 3, 4, 5]))  # Output: 6

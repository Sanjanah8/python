def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    return binary_search(arr[:min(i, len(arr))], target)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(exponential_search(arr, 7))  # Output: 6

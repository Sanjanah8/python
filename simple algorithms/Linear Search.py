def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 30))

def activity_selection(start, finish):
    n = len(finish)
    selected = []

    i = 0
    selected.append(i)

    for j in range(1, n):
        if start[j] >= finish[i]:
            selected.append(j)
            i = j

    return selected

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print(activity_selection(start, finish))  # Output: [0, 1, 3, 4]

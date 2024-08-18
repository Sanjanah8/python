def fractional_knapsack(weights, values, capacity):
    index = list(range(len(values)))
    ratio = [v / w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    for i in index:
        if weights[i] <= capacity:
            max_value += values[i]
            capacity -= weights[i]
        else:
            max_value += values[i] * (capacity / weights[i])
            break

    return max_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
``

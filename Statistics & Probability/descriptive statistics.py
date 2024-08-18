import numpy as np
import statistics

# Sample data
data = [10, 20, 30, 40, 50]

# Mean
mean = np.mean(data)
print(f"Mean: {mean}")

# Median
median = np.median(data)
print(f"Median: {median}")

# Mode
mode = statistics.mode(data)
print(f"Mode: {mode}")

# Variance
variance = np.var(data)
print(f"Variance: {variance}")

# Standard Deviation
std_dev = np.std(data)
print(f"Standard Deviation: {std_dev}")

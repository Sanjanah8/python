import numpy as np
from scipy.stats import pearsonr

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate Pearson correlation coefficient
corr_coefficient, p_value = pearsonr(x, y)

print(f"Pearson Correlation Coefficient: {corr_coefficient}")
print(f"P-Value: {p_value}")

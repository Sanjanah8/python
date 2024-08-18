from scipy import stats

# Sample data
sample1 = np.array([2, 4, 6, 8, 10])
sample2 = np.array([3, 5, 7, 9, 11])

# Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2)

print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

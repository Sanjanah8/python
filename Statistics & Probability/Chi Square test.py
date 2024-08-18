import scipy.stats as stats

# Observed frequencies
observed = np.array([10, 20, 30])

# Expected frequencies
expected = np.array([15, 15, 30])

# Perform chi-square test
chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")

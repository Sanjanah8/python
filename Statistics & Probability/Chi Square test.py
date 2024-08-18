import scipy.stats as stats

# Sample data (contingency table)
data = [[10, 20, 30], [6, 15, 20]]

# Perform Chi-Square test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(data)
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies: {expected}")

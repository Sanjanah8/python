import numpy as np
import statsmodels.api as sm

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Add constant to the predictor
X = sm.add_constant(x)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the summary
print(model.summary())

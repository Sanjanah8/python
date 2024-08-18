import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 10  # Number of trials
p = 0.5  # Probability of success

# Generate data
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

# Plot
plt.bar(x, pmf)
plt.title('Binomial Distribution PMF')
plt.xlabel('Number of successes')
plt.ylabel('Probability')
plt.show()

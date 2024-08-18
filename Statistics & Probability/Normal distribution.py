import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate a normal distribution
mean = 0
std_dev = 1
data = np.random.normal(mean, std_dev, 1000)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Plot the theoretical normal distribution
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)
plt.title('Normal Distribution')
plt.show()

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
data = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0]
])

# Standardize data
scaler = StandardScaler()
data = scaler.fit_transform(data)

# Apply PCA
pca = PCA(n_components=1)
principal_components = pca.fit_transform(data)

print("Principal Component:")
print(principal_components)

import geopandas as gpd
import matplotlib.pyplot as plt

# Load a sample shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the world map
world.plot()
plt.show()

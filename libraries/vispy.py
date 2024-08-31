import vispy.plot as vp

# Create a plot with VisPy
fig = vp.Fig()
ax = fig[0, 0]

# Plot some data
ax.plot([1, 2, 3, 4], [10, 20, 15, 25])

# Show the plot
fig.show()

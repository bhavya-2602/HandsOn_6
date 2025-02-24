import matplotlib.pyplot as plt

# Data for the benchmarks (Array sizes and corresponding times for each case)
sizes = [1000, 5000, 10000, 20000, 50000]
best_case_times = [256000, 73500, 127200, 386300, 635700]
worst_case_times = [160100, 123800, 195600, 438100, 914700]
average_case_times = [107400, 256200, 503400, 1056700, 3876600]

# Create a figure and set its size (Width: 10 inches, Height: 6 inches)
plt.figure(figsize=(10, 6))

# Plot the Best Case with green color, circular markers, and solid lines
plt.plot(sizes, best_case_times, marker='o', label='Best Case (ns)', color='green', linestyle='-')

# Plot the Worst Case with red color, circular markers, and solid lines
plt.plot(sizes, worst_case_times, marker='o', label='Worst Case (ns)', color='red', linestyle='-')

# Plot the Average Case with blue color, circular markers, and solid lines
plt.plot(sizes, average_case_times, marker='o', label='Average Case (ns)', color='blue', linestyle='-')

# Add a title to the graph
plt.title('Quicksort Benchmarking')

# Label the x-axis (Array size)
plt.xlabel('Array Size')

# Label the y-axis (Time in nanoseconds)
plt.ylabel('Time (nanoseconds)')

# Set log scale for both x and y axes to better visualize the data
plt.xscale('log')  # Logarithmic scale for x-axis (array size)
plt.yscale('log')  # Logarithmic scale for y-axis (execution time)

# Set x-axis ticks to match the array sizes for better readability
plt.xticks(sizes)

# Display a legend to explain the plotted lines
plt.legend()

# Enable grid lines for both major and minor axes, making the graph easier to read
plt.grid(True, which="both", ls="--", linewidth=0.5)

# Adjust the layout to make sure everything fits within the figure area
plt.tight_layout()

# Show the plot to the user
plt.show()


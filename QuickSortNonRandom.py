import time
import random

def benchmark(sizes):
    # Print the header for the benchmark results
    print(f"{'Size':<10} {'Best Case (ns)':<20} {'Worst Case (ns)':<20} {'Average Case (ns)':<20}")

    # Loop through each array size for benchmarking
    for n in sizes:
        # Generate best, worst, and average case arrays
        best_case = generate_best_case(n)
        worst_case = generate_worst_case(n)
        average_case = generate_average_case(n)

        # Measure the time for the best case scenario
        best_start = time.time_ns()
        quicksort(best_case, 0, len(best_case) - 1)
        best_end = time.time_ns()
        best_time = best_end - best_start

        # Measure the time for the worst case scenario
        worst_start = time.time_ns()
        quicksort(worst_case, 0, len(worst_case) - 1)
        worst_end = time.time_ns()
        worst_time = worst_end - worst_start

        # Measure the time for the average case scenario
        avg_start = time.time_ns()
        quicksort(average_case, 0, len(average_case) - 1)
        avg_end = time.time_ns()
        avg_time = avg_end - avg_start

        # Print the benchmark results for the current array size
        print(f"{n:<10} {best_time:<20} {worst_time:<20} {avg_time:<20}")

# Function to generate the best case: already sorted array
def generate_best_case(n):
    return list(range(n))

# Function to generate the worst case: reverse sorted array
def generate_worst_case(n):
    return list(range(n, 0, -1))

# Function to generate the average case: random array of integers
def generate_average_case(n):
    return [random.randint(0, n-1) for _ in range(n)]

# Quicksort algorithm implementation
def quicksort(arr, left, right):
    if left < right:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, left, right)
        
        # Recursively sort the left and right partitions
        quicksort(arr, left, pivot_index - 1)  # Left partition
        quicksort(arr, pivot_index + 1, right)  # Right partition

# Partition function to reorder the array around the pivot
def partition(arr, left, right):
    # Use the middle element as the pivot
    pivot_index = (left + right) // 2
    pivot = arr[pivot_index]
    
    # Move the pivot to the start of the array
    swap(arr, pivot_index, left)
    
    # Initialize the pointer for elements smaller than the pivot
    i = left + 1

    # Rearrange elements smaller than pivot to the left
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1

    # Place the pivot in its correct position
    swap(arr, left, i - 1)
    return i - 1

# Swap function to swap two elements in the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Main block to start the benchmarking process
if __name__ == "__main__":
    # Sizes of arrays to test
    sizes = [1000, 5000, 10000, 20000, 50000]
    
    # Call the benchmark function with the array sizes
    benchmark(sizes)

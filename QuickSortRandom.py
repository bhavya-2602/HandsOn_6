import random

def quicksort(arr, left, right):
    if left < right:
        # Partition the array and get the pivot index
        pivotIndex = partition(arr, left, right)
        
        # Recursively sort the left and right partitions
        quicksort(arr, left, pivotIndex - 1)  # Left partition
        quicksort(arr, pivotIndex + 1, right)  # Right partition

def partition(arr, left, right):
    # Choose a random pivot index
    pivotIndex = left + random.randint(0, right - left)  
    pivot = arr[pivotIndex]
    print(f"Selected Pivot: {pivot} from index {pivotIndex}")  # Display selected pivot
    
    # Move pivot to the end for partitioning
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]

    storeIndex = left  # Pointer for the smaller element
    # Move elements smaller than pivot to the left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1

    # Move pivot to its correct position
    arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
    return storeIndex  # Return pivot's final position

if __name__ == "__main__":
    arr = {45, 9, 34, 18, 5, 62, 18}  # Example array (using set)
    print("Original Array:", arr)

    # Convert the set to a list for sorting
    quicksort(list(arr), 0, len(arr) - 1)

    print("Sorted Array:", arr)

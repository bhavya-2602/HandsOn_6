import java.util.Arrays;
import java.util.Random;

public class QuicksortRandomSimplified {

    public static void main(String[] args) {
        // Example array to be sorted
        int[] arr = {45, 9, 34, 18, 5, 62, 18}; 
        System.out.println("Original Array: " + Arrays.toString(arr));
        
        // Call quicksort to sort the array
        quicksort(arr, 0, arr.length - 1);
        
        // Print the sorted array
        System.out.println("Sorted Array: " + Arrays.toString(arr));
    }

    // Quicksort method: recursively sorts the array
    public static void quicksort(int[] arr, int left, int right) {
        if (left < right) {
            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, left, right);
            
            // Recursively sort the left and right partitions
            quicksort(arr, left, pivotIndex - 1); // Left partition
            quicksort(arr, pivotIndex + 1, right); // Right partition
        }
    }

    // Partition method: rearranges elements around a pivot
    private static int partition(int[] arr, int left, int right) {
        Random random = new Random();
        
        // Select a random pivot index and print the selected pivot
        int pivotIndex = left + random.nextInt(right - left + 1);
        int pivot = arr[pivotIndex];
        System.out.println("Selected Pivot: " + pivot + " from index " + pivotIndex); // Print pivot
        
        // Move the pivot to the end of the array for partitioning
        swap(arr, pivotIndex, right);

        int storeIndex = left; // Pointer for the smaller element
        
        // Rearrange the array: elements smaller than pivot go to the left
        for (int i = left; i < right; i++) {
            if (arr[i] < pivot) {
                swap(arr, storeIndex, i);
                storeIndex++; // Increment storeIndex when a smaller element is found
            }
        }
        
        // Move pivot to its final position
        swap(arr, storeIndex, right);
        
        // Return the index where the pivot is placed
        return storeIndex;
    }

    // Swap method: swaps two elements in the array
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}


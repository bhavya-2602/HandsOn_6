import java.util.Random;
import java.util.stream.IntStream;

public class QuicksortNonRandom {
    public static void main(String[] args) {
        int[] sizes = {1000, 5000, 10000, 20000, 50000}; // Different array sizes for benchmarking
        benchmark(sizes);
    }

    private static void benchmark(int[] sizes) {
        System.out.printf("%-10s %-20s %-20s %-20s%n", "Size", "Best Case (ns)", "Worst Case (ns)", "Average Case (ns)");

        for (int n : sizes) {
            int[] bestCase = generateBestCase(n);  // Sorted array (Best case)
            int[] worstCase = generateWorstCase(n); // Reverse sorted array (Worst case)
            int[] averageCase = generateAverageCase(n); // Randomized array (Average case)

            // Measure Best Case Execution Time
            long bestStart = System.nanoTime();
            quicksort(bestCase, 0, bestCase.length - 1);
            long bestEnd = System.nanoTime();
            long bestTime = bestEnd - bestStart;

            // Measure Worst Case Execution Time
            long worstStart = System.nanoTime();
            quicksort(worstCase, 0, worstCase.length - 1);
            long worstEnd = System.nanoTime();
            long worstTime = worstEnd - worstStart;

            // Measure Average Case Execution Time
            long avgStart = System.nanoTime();
            quicksort(averageCase, 0, averageCase.length - 1);
            long avgEnd = System.nanoTime();
            long avgTime = avgEnd - avgStart;

            // Print the benchmark results
            System.out.printf("%-10d %-20d %-20d %-20d%n", n, bestTime, worstTime, avgTime);
        }
    }

    // Generates a sorted array (Best case for quicksort)
    private static int[] generateBestCase(int n) {
        return IntStream.range(0, n).toArray();
    }

    // Generates a reverse sorted array (Worst case for quicksort)
    private static int[] generateWorstCase(int n) {
        return IntStream.iterate(n - 1, i -> i - 1).limit(n).toArray();
    }

    // Generates a random array (Average case for quicksort)
    private static int[] generateAverageCase(int n) {
        return new Random().ints(n, 0, n).toArray();
    }

    // Recursive quicksort function
    public static void quicksort(int[] arr, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(arr, left, right);
            quicksort(arr, left, pivotIndex - 1); // Sort left partition
            quicksort(arr, pivotIndex + 1, right); // Sort right partition
        }
    }

    // Partitions the array and returns the pivot index
    private static int partition(int[] arr, int left, int right) {
        int pivotIndex = left + (right - left) / 2; // Middle element as pivot
        int pivot = arr[pivotIndex];
        swap(arr, pivotIndex, left); // Move pivot to the start
        int i = left + 1, j = right;

        // Rearrange elements around the pivot
        while (i <= j) {
            while (i <= right && arr[i] < pivot) i++;
            while (j >= left && arr[j] > pivot) j--;
            if (i <= j) swap(arr, i++, j--);
        }
        swap(arr, left, j); // Place pivot in its correct position
        return j;
    }

    // Swaps two elements in the array
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}


import java.util.Arrays;

public class ArrayValidity {

    // Function to find the validity of an array
    public static int findValidity(int[] arr) {
        int minValidity = Integer.MAX_VALUE; // Initialize with maximum possible value

        // Generate all subsequences of size 3
        for (int i = 0; i < arr.length - 2; i++) {
            for (int j = i + 1; j < arr.length - 1; j++) {
                for (int k = j + 1; k < arr.length; k++) {
                    // Subsequence of three elements
                    int[] subsequence = { arr[i], arr[j], arr[k] };

                    // Calculate validity for this subsequence
                    int validity = calculateValidity(subsequence);
                    // System.out.print(validity);
                    // Update minimum validity if necessary

                    minValidity = Math.min(minValidity, validity);
                }
            }
        }

        return minValidity;
    }

    // Helper function to calculate validity for a given subsequence of three
    // elements
    private static int calculateValidity(int[] subsequence) {
        Arrays.sort(subsequence); // Sort to easily find the median
        double mean = (subsequence[0] + subsequence[1] + subsequence[2]) / 3.0;
        double median = subsequence[1]; // Middle element after sorting
        return (int) (3 * Math.abs(mean - median));
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 4, 5 };
        System.out.println("Minimum validity: " + findValidity(arr));
    }
}

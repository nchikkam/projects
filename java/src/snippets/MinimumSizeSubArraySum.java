package snippets;

public class MinimumSizeSubArraySum {
    // Returns length of smallest subarray with sum greater than x.
    // If there is no subarray with given sum, then returns n+1
    public static int smallestSubWithSum(int arr[], int x){
        int start = -1,
            sum = 0,
            min_size = Integer.MAX_VALUE;

        for (int i = 0; i < arr.length; ++i) {
            sum += arr[i];
            while (sum >= x) {
                min_size = Math.min(min_size, i - start);
                sum -= arr[++start];
            }
        }
        if (min_size == Integer.MAX_VALUE) {
            return 0;
        }
        return min_size;
    }

    public static void main(String[] args) {
        int arr1[] = {1, 4, 45, 6, 10, 19};
        int x = 51;
        System.out.println(smallestSubWithSum(arr1, x));

        int arr2[] = {1, 10, 5, 2, 7};
        x = 9;
        System.out.println(smallestSubWithSum(arr2, x));

        int arr3[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250};
        x = 280;
        System.out.println(smallestSubWithSum(arr3, x));
    }
}
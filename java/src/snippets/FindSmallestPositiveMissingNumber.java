package snippets;

import java.util.Arrays;

public class FindSmallestPositiveMissingNumber {

    /*
        Idea:
        This problem can solve by using a bucket-sort like algorithm. Let's
        consider finding first missing positive and 0 first. The key fact is
        that the ith element should be i, so we have:
        i==A[i]
        A[i]==A[A[i]]
    */
    public static int firstMissingPositive(int[] A) {  // leecode
        int n = A.length;

        for (int i = 0; i < n; i++) {
            // when the ith element is not i
            while (A[i] != i + 1) {
                // no need to swap when ith element is out of range [0,n]
                if (A[i] <= 0 || A[i] >= n)
                    break;

                //handle duplicate elements
                if(A[i]==A[A[i]-1])
                    break;

                //swap
                int temp = A[i];
                A[i] = A[temp - 1];
                A[temp - 1] = temp;
            }
        }

        for (int i = 0; i < n; i++){
            if (A[i] != i + 1){
                return i + 1;  // critical to return +1
            }
        }
        return n + 1;
    }

    /*
        If we see element 'x', we make the element at pos_half(x) negative.
        Then we traverse the positive half again to look for 1st negative value. The
        index  of  that  value is the smallest positive element missing in the array.
        See the implementation below.
    */
    public static void swap(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    public static int moveNegativesToLeft(int a[]){
        int j = 0, i;
        for(i = 0; i < a.length; i++){
            if (a[i] <= 0){
                swap(a, i, j);
                j++;
            }
        }
        return j;
    }
    public static int findPositive(int arr[], int start, int n){
        int i;

        // Mark arr[i] as visited by making arr[arr[i] - 1] negative.
        for(i = start; i < n; i++){
            if(Math.abs(arr[i]) - 1 < n && arr[Math.abs(arr[i]) - 1] > 0)
                arr[Math.abs(arr[i]) - 1] = -arr[Math.abs(arr[i]) - 1];
        }
        // Return the first index value at which is positive
        for(i = start; i < n; i++)
            if (arr[i] > 0)
                return i+1;
        return n+1;
    }

    public static int findMissingSmallestPositive(int a[]){
        int neg = moveNegativesToLeft(a);  // position of first -ve
        return findPositive(a, neg, a.length);
    }

    public static void main(String[] args){
        int a[] = {3, 4, -1, 1};
        System.out.println(firstMissingPositive(a));
        System.out.println(findMissingSmallestPositive(a));

        int b[] = {1, 2, 0};
        System.out.println(firstMissingPositive(b));
        System.out.println(findMissingSmallestPositive(b));

        int c[] = { -8, 3, 2, -4, 6, 1, 5};
        System.out.println(firstMissingPositive(c));
        System.out.println(findMissingSmallestPositive(c));
    }
}
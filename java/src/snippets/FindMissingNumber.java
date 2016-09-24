package snippets;

import java.util.Arrays;

public class FindMissingNumber {

    public static int findMissingNumberUsingFormula(int[] a, int n){
        if(n <= 0) return -1;
        int sum1 = 0;
        for(int i = 0; i < n; ++i)
            sum1 += a[i];
        int sum2 = n * (n + 1) / 2;
        return sum2 - sum1;
    }

    public static int getMissingNumberSorted(int[] a, int n){  // Sorted array
        if( n <= 0) return -1;
        int left = 0;
        int right = n - 1;
        while(left <= right){
            int middle = (right + left) / 2;
            if(a[middle] != middle){           // critical part
                if(middle == 0 || a[middle - 1] == middle - 1)
                    return middle;
                right = middle - 1;
            }
            else
                left = middle + 1;
        }
        return -1;
    }

    public static void main(String [] args){
        int a[] = {0, 1, 2, 3, 4, 6, 7, 8, 9, 10};
        System.out.println(findMissingNumberUsingFormula(a, a.length));

        Arrays.sort(a);
        System.out.println(getMissingNumberSorted(a, a.length));
    }
}
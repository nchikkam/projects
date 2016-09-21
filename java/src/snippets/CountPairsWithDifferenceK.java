package snippets;

import java.util.Arrays;

public class CountPairsWithDifferenceK {

    public static int countPairsWithDifferenceK(int a[], int k){
        Arrays.sort(a); // qsort the array
        int l = 0;
        int r = 0;
        int count = 0;
        int n = a.length;
        while(r < n){
            if(a[r] - a[l] == k){// diff is 'k'
                count++;
                l++;
                r++;
            }else if(a[r] - a[l] > k)
                l++;
            else
                r++;
        }
        return count;
    }

    public static void main(String [] args){
        int a[] = {7, 6, 23, 19, 10, 11, 9, 3, 15};
        System.out.println(countPairsWithDifferenceK(a, 4));

    }
}
package snippets;

import java.util.Arrays;
import java.util.Hashtable;

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

    public static int countPairsWithDifferenceKHash(int a[], int k){
        int count = 0;
        Hashtable<Integer, Integer> map = new Hashtable<Integer, Integer>();

        for(int i = 0; i < a.length; i++)  // store all entries in hash
            map.put(a[i], 1);

        for(int i = 0; i < a.length; i++){
            if(map.containsKey(a[i]+k))
                count++;
        }
        return count;
    }

    public static void main(String [] args){
        int a[] = {7, 6, 23, 19, 10, 11, 9, 3, 15};
        System.out.println(countPairsWithDifferenceK(a, 4));
        System.out.println(countPairsWithDifferenceKHash(a, 4));

        int [] b = {1, 3, 5, 6, 9};
        System.out.println(countPairsWithDifferenceK(a, 2));
        System.out.println(countPairsWithDifferenceKHash(a, 2));
    }
}
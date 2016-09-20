package snippets;

import java.util.Arrays;

public class PairsSumToZero {

    public static int binSearch(int [] a, int key){
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi){
            int mid = lo + (hi - lo) / 2;
            if (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

    public static int countPairsSumToZero(int [] a){
        Arrays.sort(a);
        int count = 0;
        for(int i =0; i < a.length; i++){
            int found = binSearch(a, -a[i]);
            if(found > i){  // critical part
                count += 1;
            }
        }
        return count;
    }

    public static void main(String [] args){
        int [] a = {4, 1, 2, 3, -4, 5, 6, 7, 8, -5, -2, -7};
        System.out.println(countPairsSumToZero(a));
    }
}
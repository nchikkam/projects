package snippets;

import java.util.Arrays;

public class FindPairCloseToZero {

    public static int [] findPair(int [] a){
        int l, r , min_sum, sum = 0, min_l, min_r;
        int n = a.length;

        if(n < 2) return a;
        Arrays.sort(a);

        l = 0; r = n-1;
        min_sum = a[l] + a[r];
        min_l = l;
        min_r = r;

        while(l < r){
            sum = a[l] + a[r];

            if(Math.abs(sum) < Math.abs(min_sum)){
                min_sum = sum;
                min_l = l;
                min_r = r;
            }
            if(sum < 0)
                l++;
            else
                r--;
        }
        return new int[]{min_l, min_r};
    }

    public static void main(String [] args){
        int a[] = {-45, -20, -2, -1, 12, 15, 30};
        int data [] = findPair(a);
        System.out.println(data[0]);
        System.out.println(data[1]);
    }
}
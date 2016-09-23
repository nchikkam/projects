package snippets;

import java.util.Arrays;
import java.util.Hashtable;

public class PythogoreanTriplets {

    public static int countPythogoreanTriplets_O_N_3(int [] a){
        int count = 0;
        for(int i=0; i < a.length; i++){
            for(int j =i+1; j < a.length; j++){
                for( int k = j+1; k< a.length; k++ ) {
                    int a2 = a[i]*a[i];
                    int b2 = a[j]*a[j];
                    int c2 = a[k]*a[k];
                    if(a2 == b2+c2 ||b2 == a2+c2 || c2 == a2+b2)
                        count += 1;
                }
            }
        }
        return count;
    }

    public static int countPythogoreanTriplets_O_N_2(int [] a){  // O(N) space
        Hashtable<Integer, Integer> map = new Hashtable<Integer, Integer>();
        for(int v: a)
            map.put(v*v, 1);

        int count = 0;
        for(int i=0; i < a.length; i++){
            for(int j =i+1; j < a.length; j++){
                int a2 = a[i]*a[i];
                int b2 = a[j]*a[j];
                if (map.containsKey(a2+b2))
                    count += 1;
            }
        }
        return count;
    }

    public static int countPythogoreanTriplets_O_N_2_S_N_2(int [] a){  // O(N^2) space
        Hashtable<Integer, Integer> map = new Hashtable<Integer, Integer>();
        for(int i=0; i < a.length; i++){
            int a2 = a[i]*a[i];
            for(int j =i+1; j < a.length; j++) {
                int b2 = a[j]*a[j];
                map.put(a2+b2, 1);
            }
        }

        int count = 0;
        for(int i=0; i < a.length; i++){
            int c2 = a[i]*a[i];
            if (map.containsKey(c2))
                count += 1;
        }
        return count;
    }

    public static int countPythogoreanTriplets_O_N_2_NoExtraSpace(int a[]){
        for (int i=0; i<a.length; i++)
            a[i] = a[i]*a[i];
        Arrays.sort(a);

        int count = 0;
        for (int i = a.length-1; i >= 2; i--){
            int left = 0;   // index of the first element in arr[0..i-1]
            int right = i-1; // index of the last element in arr[0..i-1]
            while (left < right){
                // A triplet found
                if (a[left] + a[right] == a[i])
                    count +=1;

                if (a[left] + a[right] < a[i])
                    left++;
                else
                    right--;
            }
        }
        return count;
    }

    public static void main(String [] args){
        int [] a = {1, 3, 4, 5, 6, 7, 8, 10, 11};

        System.out.println(countPythogoreanTriplets_O_N_3(a));  //2 [ 3,4,5], [6,8,10]
        System.out.println(countPythogoreanTriplets_O_N_2(a));
        System.out.println(countPythogoreanTriplets_O_N_2_S_N_2(a));
        System.out.println(countPythogoreanTriplets_O_N_2_S_N_2(a));
        System.out.println(countPythogoreanTriplets_O_N_2_NoExtraSpace(a));
    }
}
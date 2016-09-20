package snippets;

import java.util.Arrays;

public class TriplesSumToZero {

    public static int countTriplesSumToZero(int [] a){
        Arrays.sort(a);
        int count = 0;
        for(int i =0; i < a.length; i++){
            for(int j =i+1; j < a.length; j++) {
                int found = PairsSumToZero.binSearch(a, -a[i] - a[j]);
                if (found > j) {  // critical part
                    System.out.println(a[i] + " " + a[j] +" " + (-a[i]-a[j]));
                    count += 1;
                }
            }
        }
        return count;
    }

    public static void main(String [] args){
        int [] a = {4, 1, 2, 3, -4, 5, 6, 7, 8, -5, -2, -7};
        System.out.println(countTriplesSumToZero(a));
    }
}
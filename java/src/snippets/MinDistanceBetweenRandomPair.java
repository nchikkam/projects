package snippets;

import java.util.Arrays;

public class MinDistanceBetweenRandomPair {

    public static int [] minDistance(int [] a){
        Arrays.sort(a); //O(NlogN)  mid distance will be betweek each consequtive pair
        int min = Integer.MAX_VALUE;
        int one=-1, two=-1;
        for(int i=1;i<a.length; i++){
            int temp = a[i]-a[i-1];
            if( min > temp){
                min = temp;
                one = a[i];
                two = a[i-1];
            }
        }
        return new int[]{min, one, two};
    }

    public static void main(String[] args){
        int a[] = {1, 2, 0, 8, 1, 9, 9, 3};
        int [] data = minDistance(a);
        System.out.println("Distance: "+ data[0]);
        System.out.println("One: "+ data[1]);
        System.out.println("Two: "+ data[2]);
    }
}
package snippets;

public class MaximizeAi_i_Aj_j {

    // Returns maximum value of (arr[i]-i) - (arr[j]-j)
    // max(ai-i) - min(aj-h
    public static int findMaxDiff(int a[]){
        int n = a.length;
        if (n < 2)
            return 0;

        int min_val = Integer.MAX_VALUE, max_val = Integer.MIN_VALUE;
        for (int i=0; i<n; i++){
            if ((a[i]-i) > max_val)
                max_val = a[i] - i;
            if ((a[i]-i) < min_val)
                min_val = a[i]-i;
        }
        return (max_val - min_val);
    }

    public static void main(String []args){
        int [] a = {9, 15, 4, 12, 13};
        System.out.println(findMaxDiff(a)); //(15 - 1) - (4 - 2) = 12

        int []b = {-1, -2, -3, 4, 10};
        System.out.println(findMaxDiff(b)); //(10 - 4) - (-3 - 2) = 11
    }
}
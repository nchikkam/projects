package snippets;

public class MaxSumContiguousSunArrayKadanes {

    public static int maxSum(int a[]){
        int maxSum = 0,sum = 0;
        int i;
        for(i = 0;i<a.length;i++){
            sum = sum + a[i];
            if(sum < 0)  // start a new sum, previous accumulation doesn't help
                sum = 0;
            else if(sum > maxSum)
                maxSum = sum;
        }
        return maxSum;
    }

    public static void main(String[] args){
        int a[] = {11, -12, 15, -3, 8, -9, 1, 8, 10, -2};
        System.out.println(maxSum(a));
    }
}
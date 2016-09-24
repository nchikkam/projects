package snippets;

public class SubArraySumEqualsK {

    /*
        bool isGroupSum(int *arr, int target, int start){
          if(start >= arr.length)
                return (target == 0);
          //we found the target sum, return true
          if(target == 0)
                return true;
          //else, check if sum can be obtained by any of the following
          //      1) Including the current element
          //      2) Excluding the current element
          return isGroupSum(arr, target - arr[start], start+1)
                   || isGroupSum(arr, target,start+1);
        }
    */

    public static int getGroupSum(int []arr, int target){
        int n = arr.length;
        int rem_sum = arr[0], start = 0, i;
        for (i = 1; i <= n; i++){
            while(rem_sum > target && start < i-1){
                rem_sum = rem_sum - arr[start];
                start++;
            }
            if(rem_sum == target){
                System.out.println( start );
                System.out.println( i-1 );
                return 1;
            }
            if(i < n)
                rem_sum = rem_sum + arr[i];
        }

        System.out.println("No sub array with target sum");
        return 0;
    }

    public static void main(String[] args){
        int a[] =  {2, 4, 8};
        getGroupSum(a, 12);
        getGroupSum(a, 10);
    }
}
package snippets;

public class MissingTwoNumbersFinder {


    public static int [] findMissingNumbers(int [] a){
        int xor = 0;
        // xor array
        for (int n: a)
            xor ^= n;

        // xor all n for 1<= i <= n
        for(int i =1; i <= a.length+2; i++)
            xor ^= i;

        xor = xor & ~(xor-1);  // right most set bit
        int x = 0, y = 0;

        for( int n: a){
            if ((n & xor) > 0)
                x ^= n;
            else
                y ^= n;
        }

        for(int i =1; i <= a.length+2; i++) {
            if ((i & xor) > 0)
                x ^= i;
            else
                y ^= i;
        }

        return new int[]{
            x, y
        };
    }

    public static void main(String[] args){
        int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

        int [] nums = findMissingNumbers(a);
        System.out.println(nums[0] + " " + nums[1]);
    }
}

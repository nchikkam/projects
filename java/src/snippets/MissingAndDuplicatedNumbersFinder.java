package snippets;

public class MissingAndDuplicatedNumbersFinder {

    public static int [] findMissingNumbers(int [] a){
        int xor = 0;
        // xor array
        for (int n: a)
            xor ^= n;

        // xor all n for 1<= i <= n
        for(int i =1; i <= a.length; i++)   // duplicate, the logic is same except that loop runs till length times.
            xor ^= i;

        xor = xor & ~(xor-1);  // right most set bit
        int x = 0, y = 0;

        for( int n: a){
            if ((n & xor) > 0)
                x ^= n;
            else
                y ^= n;
        }

        for(int i =1; i <= a.length; i++) {
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
        int a[] = {3, 1, 3};
        int []data = findMissingNumbers(a);
        System.out.print(data[0] + " " + data[1]);

        System.out.println();

        int b[] = {4, 3, 6, 2, 1, 1};
        int []d = findMissingNumbers(b);
        System.out.print(d[0] + " " + d[1]);
    }
}
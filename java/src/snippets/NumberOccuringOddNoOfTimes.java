package snippets;

public class NumberOccuringOddNoOfTimes {

    public static int findNumberOccuringOddNoOfTimes(int[] a){
        // clue is 0 XOR X = X
        // e.g:    0000 ^ 0010 = 0010 (!a & b) + (!b & a)
        int xor = 0;
        for(int v: a)
            xor ^= v;
        return xor;
    }

    public static void main(String [] args){
        int [] a= {1, 4, 6, 7, 3, 1, 4, 7, 3, 1, 6};
        System.out.println(findNumberOccuringOddNoOfTimes(a));

        int [] b= {1};
        System.out.println(findNumberOccuringOddNoOfTimes(b));

        int [] c= {1, -2, 3, 3, 1};
        System.out.println(findNumberOccuringOddNoOfTimes(c));

        int [] d= {1, -2, -3, -3, -1, -1, 1};
        System.out.println(findNumberOccuringOddNoOfTimes(c));
    }
}
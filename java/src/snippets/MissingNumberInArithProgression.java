package snippets;

public class MissingNumberInArithProgression {

    public static int findMissing(int [] a, int d){
        // elementsin a are in arithmetic progression and unordered
        int sum = 0;
        int min = Integer.MAX_VALUE;
        for( int v: a) {
            sum += v;
            if (min > v)
                min = v;
        }

        //n/2*(2a+(n-1)*d)
        int n = a.length+1;
        int realSum = (n/2) * (2*min + (n-1)*d);
        return (realSum-sum);
    }

    public static void main(String [] args){
        int a[] = {1, 11, 3, 9, 5}; // 7 missing 2 is d
        System.out.println(findMissing(a, 2));
    }
}
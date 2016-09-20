package snippets;

public class Combinations {

    public static void swap(char[]a , int i, int j){
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void combinations(
            char[] a,   // actual chars
            int pos,    // to fill selector
            int start,  // to process char
            int k,      // cardinality
            char[] basket){  // basket to keep selection
        if( k == 0 ){
            int j;
            for( j=0;j < pos;++j)
                System.out.print(basket[j]);
            System.out.println();
            return;
        }
        for(int i=start;i<=(a.length-k);++i){
            basket[pos] = a[i];
            combinations(a, pos+1, i+1, k-1, basket);
        }
    }

    public static void main(String[] args){
        char [] c = {'a', 'b', 'c', 'd'};
        char [] basket = new char[c.length];
        for( int k =0; k < c.length; k++)
            combinations(c, 0, 0, k, basket);
    }
}
package snippets;

public class ProductOfOtherElements {

    public static int [] product(int a[]){
        int prod[] = new int[a.length];
        prod[prod.length-1] = 1;

        for(int i=a.length-2; i>=0; i--)
            prod[i] = prod[i+1] * a[i+1];

        int left = 1;
        for(int i=0; i<a.length; i++) {
            prod[i] *= left;
            left *= a[i];
        }
        return prod;
    }

    public static void main(String [] args){
        int a[] = {1, 2, 3, 4};
        int r[] = product(a);
        for(int i: r)
            System.out.println(i);
    }
}
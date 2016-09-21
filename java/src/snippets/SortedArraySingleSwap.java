package snippets;

public class SortedArraySingleSwap {

    public static void swap(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    public static void sortAlmostSortedArrayWithSingleSwap(int [] a){
        // sorted but one pair is swapped
        int right = a.length-1;
        while( right > 0 && (a[right] > a[right-1]))   // first find the first disorder element
            right--;

        int j = right-1;
        while (j>=0 && a[right] < a[j])   // find the disordered element proper location
            j--;

        swap(a, right, j+1);
    }

    public static void main(String[] args){
        int [] a = {1, 2, 9, 4, 5, 6, 7, 8, 3};
        sortAlmostSortedArrayWithSingleSwap(a);
        for(int v: a){
            System.out.print(v+ " ");
        }
    }
}
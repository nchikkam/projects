package snippets;

public class QuickSort {

    private static void swap(int []a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // O(NlogN) algorithm to sort an array, basically it uses divide
    // and conquer approach to prepare the array into two parts w.r.t
    // an element called pivot that directs the recursion into two
    // parts to sort left sublist and right sublist.
    public  static void qSort(int A[], int start, int end){
        int last;
        if ( start >= end) return;
        swap(A, start, (start+end)/2);
        last = start;
        for(int i=start+1; i <=end; i++){
            if (A[i] < A[start]) {
                last += 1;
                swap(A, last, i);
            }
        }
        swap(A, start, last);
        qSort(A, start, last-1);
        qSort(A, last+1, end);

    }

    public static void main(String [] args){
        int [] a = {2, 6, 5, 1, 3, 4};
        qSort(a, 0, a.length-1);

        for(int v: a)
            System.out.print(v + " ");
        System.out.println();
    }
}
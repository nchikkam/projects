package snippets;

public class KthElementFinder {
    /*
            Idea: qsort pivot logic
            keep two pointers l, r l moves to right , r moves to left
            While l and r don't reach or coincide:
                Choose element at a[k] as pivot
                find i, j where they satisfy:
                    a[i] < pivot < a[j] by ++i and --j
                if i <= j:
                    swap a[i], a[j]
                    ++i, --j
                update l, r based on i, j as below:
                if i > k: r = j
                if j < k: l = i

            return pivot
    */
    public static void swap(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static int kthElement(int [] a, int k){
        int n = a.length;
        int l =0, r = n-1;

        int pivot = a[k];
        int i, j;

        while (l < r){
            pivot = a[k];  // record the pivot, it will always be at kth spot
            i = l;
            j = r;
            // spot the pivot location
            while(a[i] < pivot) ++i;
            while(pivot < a[j]) --j;
            if (i <= j){
                swap(a, i, j);
                i++;
                j--;
            }
            if (j < k) l = i;
            if (i > k) r = j;
        }
        return pivot;
    }

    public static void main(String[] args){
        int a[] = {2, 4, 1, 6, 7, 9, 8, 5, 3};
        System.out.println(kthElement(a, 8));
    }
}
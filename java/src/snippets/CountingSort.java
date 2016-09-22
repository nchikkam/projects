package snippets;

public class CountingSort {

    public static void countingSort(int a[], int range){
        // The output array that will have sorted  arr
        int output[] = new int [a.length];

        // Create a count array to store count of individual element and
        // initialize count array as 0
        int count[] = new int [range +1],
                i;
        // Store count of each element
        for(i = 0;  i < a.length; ++i)
            ++count[a[i]];

        /* modified count array indicates the position of each object in
        the output sequence. */
        for (i = 1; i <= range; ++i)
            count[i] += count[i-1];

        // Build the output array
        for (i = 0;  i < a.length; ++i){
            output[count[a[i]]-1] =  a[i];
            --count[a[i]];
        }

        // Copy the output array to  arr
        for (i = 0;  i< a.length; ++i)
            a[i] = output[i];
    }

    public static void main(String [] args){
        int a[] = {4, 2, 1, 3, 7, 2, 2, 9, 8};
        countingSort(a, 10);
        for( int v: a)
            System.out.print(v);
        System.out.println();
    }
}
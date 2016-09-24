package snippets;

public class MoveZerosToEnd {
    public static void pushZerosToEnd(int arr[]){
        int count = 0;  // Count of non-zero elements

        // Traverse the array. If element encountered is
        // non-zero, then replace the element at index 'count'
        // with this element
        for (int i = 0; i < arr.length; i++)
            if (arr[i] != 0)
                arr[count++] = arr[i]; // here count is
        // incremented

        // Now all non-zero elements have been shifted to
        // front and 'count' is set as index of first 0.
        // Make all elements 0 from count to end.
        while (count < arr.length)
            arr[count++] = 0;
    }

    public static void main(String [] args){
        int a[] = {1, 9, 0, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9};
        pushZerosToEnd(a);
        for(int v: a)
            System.out.print(v + " ");
        System.out.println();
    }
}
package snippets;

public class RemoveDuplicatesInSortedArray {

    public static void removeDuplicates(int a[]){
        int i, distincts = 0;
        int n = a.length;

        // Remove the duplicates ...
        for (i = 1; i < n; i++)
            if (a[i] != a[distincts]) {
                distincts++;
                a[distincts] = a[i]; // Move it to the front distincts keeps position
            }

        for(i = 0; i<= distincts; i++)
            System.out.print(a[i]);
        System.out.println();
    }

    public static void main(String[] args){
        int a[] = {1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 9};
        removeDuplicates(a);

        int b[] = {1, 1, 2, 3, 5, 6, 6, 7, 10, 25, 100, 123, 123};
        removeDuplicates(b);
    }
}
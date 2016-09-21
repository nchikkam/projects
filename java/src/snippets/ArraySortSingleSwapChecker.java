package snippets;

public class ArraySortSingleSwapChecker {
    public static boolean verify(int []a){
        // given an almost sorted array, check if single swap would make it sorted
        SortedArraySingleSwap.sortAlmostSortedArrayWithSingleSwap(a);
        for(int i=0; i<a.length-2; i++)
            if (a[i] > a[i+1])
                return false;
        return true;
    }
}
package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.SortedArraySingleSwap;

public class SortedArraySingleSwapTests {
    @Test
    public void testAlmostSortedArraySingleSwap(){
        int [] a = {1, 2, 9, 4, 5, 6, 7, 8, 3};
        SortedArraySingleSwap.sortAlmostSortedArrayWithSingleSwap(a);
        for(int i =1; i< a.length; i++){
            Assert.assertTrue(
                    a[i-1] < a[i]
            );
        }
    }

    @Test
    public void testAlmostSortedSmallArraySingleSwap(){
        int [] a = {1, 5, 3};
        SortedArraySingleSwap.sortAlmostSortedArrayWithSingleSwap(a);
        for(int i =1; i< a.length; i++){
            Assert.assertTrue(
                    a[i-1] < a[i]
            );
        }
    }

    @Test
    public void testAlmostSortedAnotherArraySingleSwap(){
        int [] a = {3, 1};
        SortedArraySingleSwap.sortAlmostSortedArrayWithSingleSwap(a);
        for(int i =1; i< a.length; i++){
            Assert.assertTrue(
                    a[i-1] < a[i]
            );
        }
    }
}
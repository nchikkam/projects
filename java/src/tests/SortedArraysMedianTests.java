package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.SortedArraysMedian;

public class SortedArraysMedianTests {

    @Test
    public void testSortedListsMedian(){
        int [] one = {10, 30, 40, 50, 60, 70};
        int [] two = {30, 55, 100, 110, 115, 135};
        Assert.assertEquals(
            SortedArraysMedian.findMedianSortedArrays(one, two),
            57.5
        );
    }
}
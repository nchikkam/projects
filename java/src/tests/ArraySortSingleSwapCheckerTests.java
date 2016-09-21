package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.ArraySortSingleSwapChecker;

public class ArraySortSingleSwapCheckerTests {
    @Test
    public void test(){
        int [] a = {1, 2, 6, 3, 4, 5};
        Assert.assertFalse(
            ArraySortSingleSwapChecker.verify(a)
        );
    }
}
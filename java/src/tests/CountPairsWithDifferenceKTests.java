package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.CountPairsWithDifferenceK;

public class CountPairsWithDifferenceKTests {
    @Test
    public void test(){
        int a[] = {7, 6, 23, 19, 10, 11, 9, 3, 15};
        Assert.assertEquals(
                CountPairsWithDifferenceK.countPairsWithDifferenceK(a, 4),
                6
        );
    }
}
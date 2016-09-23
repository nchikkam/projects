package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.MinimumSizeSubArraySum;

public class MinimumSizeSubArraySumTests {

    @Test
    public void testMinimumSizeSubArraySum(){
        int [] a = {2,3,1,2,4,3};
        int s = 7;
        Assert.assertEquals(
            MinimumSizeSubArraySum.smallestSubWithSum(a, s),
            2
        );
    }

    @Test
    public void test(){
        int [] a = {2,1,3,1,1,8,3};
        int s = 4;
        Assert.assertEquals(
                MinimumSizeSubArraySum.smallestSubWithSum(a, s),
                2
        );
    }
}
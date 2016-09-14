package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.ThirdBiggest;

public class ThirdBiggestTests {

    @Test
    public void testThirdBiggestWithSortedArray() throws Exception{
        int [] a = {1, 7, 3, 9, 5, 6, 2, 8, 4};

        Assert.assertEquals(
                7,
                ThirdBiggest.findThirdBiggest(a),
                "Expectation doesn't met for Sorted Array");
    }

    @Test
    public void testWithThreeElementArray() throws Exception{
        int [] a = {1, 5, 7};

        Assert.assertEquals(
                1,
                ThirdBiggest.findThirdBiggest(a),
                "Expectation doesn't met for Sorted Array");
    }

    @Test(expectedExceptions = Exception.class)
    public void testWithInvalidArrayLength() throws Exception{
        int [] a = {1};

        ThirdBiggest.findThirdBiggest(a);
    }
}
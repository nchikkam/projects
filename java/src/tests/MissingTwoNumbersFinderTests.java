package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.MissingTwoNumbersFinder;

public class MissingTwoNumbersFinderTests {

    @Test
    public void testSmallArray(){
        int a[] = {1, 3, 5};

        int [] nums = MissingTwoNumbersFinder.findMissingNumbers(a);
        Assert.assertEquals(2, nums[0]);
        Assert.assertEquals(4, nums[1]);
    }

    @Test
    public void testArray(){
        int a[] = {1, 3, 4, 5, 7, 8, 9};

        int [] nums = MissingTwoNumbersFinder.findMissingNumbers(a);
        Assert.assertEquals(2, nums[0]);
        Assert.assertEquals(6, nums[1]);
    }
}
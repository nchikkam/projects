package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.LongestIncreasingSubSequence;

public class LongestIncreasingSubSequenceTests {

    @Test
    public void testLiss(){
        Integer[] a = {7, 2, 8, 1, 3, 4, 10, 6, 9, 5};

        Assert.assertEquals(
                LongestIncreasingSubSequence.liss(a),
                5
        );
    }
}
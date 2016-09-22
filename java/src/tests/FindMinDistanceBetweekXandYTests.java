package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.FindMinDistanceBetweenXandY;

public class FindMinDistanceBetweekXandYTests {
    @Test
    public void testCase(){
        int []a = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3, 6};
        Assert.assertEquals(
                FindMinDistanceBetweenXandY.findMinDistance(a, 3, 6),
                1
        );

        int []b = {2, 5, 3, 5, 4, 4, 2, 3};
        Assert.assertEquals(
                FindMinDistanceBetweenXandY.findMinDistance(b, 3, 2),
                1
        );

        int []c = {3, 4, 5};
        Assert.assertEquals(
                FindMinDistanceBetweenXandY.findMinDistance(c, 3, 5),
                2
        );

        int []d = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3};
        Assert.assertEquals(
                FindMinDistanceBetweenXandY.findMinDistance(d, 3, 6),
                4
        );
    }
}
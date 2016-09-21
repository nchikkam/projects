package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.PeakElement;

public class PeakElementTests {

    @Test
    public void testPeak(){
        int [] a = {1, 2, 6, 5, 3, 7, 4};
        Assert.assertEquals(
                PeakElement.peak(a, 0, a.length),
                2
        );
    }

    @Test
    public void testSteepPeak(){
        int [] a = {1, 2, 3, 4, 5, 6, 7};
        Assert.assertEquals(
                PeakElement.peak(a, 0, a.length),
                6
        );
    }

    @Test
    public void testReveseSteepPeak(){
        int [] a = {7, 6, 5, 4, 3, 2, 1};
        Assert.assertEquals(
                PeakElement.peak(a, 0, a.length),
                0
        );
    }
}
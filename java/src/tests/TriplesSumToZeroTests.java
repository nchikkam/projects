package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.TriplesSumToZero;

public class TriplesSumToZeroTests {
    @Test
    public void testPairsSum(){
        int [] a = {4, 1, 2, 3, -4, 5, 6, 7, 8, -5, -2, -7};
        Assert.assertEquals(
            TriplesSumToZero.countTriplesSumToZero(a),
            8
        );
    }
}
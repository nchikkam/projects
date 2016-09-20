package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.PairsSumToZero;

public class PairsSumToZeroTests {

    @Test
    public void testPairsSum(){
        int [] a = {4, 1, 2, 3, -4, 5, 6, 7, 8, -5, -2, -7};
        Assert.assertEquals(
                PairsSumToZero.countPairsSumToZero(a),
                4
        );
    }

    @Test
    public void testBasicPairsSum(){
        int [] a = {7, -7};
        Assert.assertEquals(
                PairsSumToZero.countPairsSumToZero(a),
                1
        );
    }

    @Test
    public void testNegativeCaseBasicPairsSum(){
        int [] a = {7, -3};
        Assert.assertEquals(
                PairsSumToZero.countPairsSumToZero(a),
                0
        );
    }
}
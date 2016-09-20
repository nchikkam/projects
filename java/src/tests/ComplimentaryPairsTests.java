package tests;

import org.testng.annotations.Test;
import org.testng.Assert;
import snippets.ComplementaryPairs;

import static org.testng.Assert.assertFalse;
import static org.testng.Assert.assertTrue;


public class ComplimentaryPairsTests {
    @Test
    public void verifyComplimentaryPairsFor2Elements(){
        int []a = {1, 2};
        ComplementaryPairs obj = new ComplementaryPairs();
        int []basket = {-1, -1};
        assertTrue(obj.findComplimentaryPair_O_NlogN(a, 3, basket));
    }

    @Test
    public void verifyComplimentaryPairsForEmptyArray(){
        int []a = {};
        ComplementaryPairs obj = new ComplementaryPairs();
        int []basket = {-1, -1};
        assertFalse(obj.findComplimentaryPair_O_NlogN(a, 3, basket));
    }

    @Test
    public void verifyComplimentaryPairsAnotherArray(){
        int []a = {30, 1, 2, 3, 4, 5,28};
        ComplementaryPairs obj = new ComplementaryPairs();
        int []basket = {-1, -1};
        assertFalse(obj.findComplimentaryPair_O_NlogN(a, 11, basket));
    }

    @Test
    public void verifyComplimentaryPairsNegativeValues(){
        int []a = {30, -1, 2, 3, 4, 5, -28};
        ComplementaryPairs obj = new ComplementaryPairs();
        int []basket = {-1, -1};
        assertTrue(obj.findComplimentaryPair_O_NlogN(a, -29, basket));
    }
}
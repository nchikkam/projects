package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.SubtractSubStrings;

public class SubtractSubStringsTests {

    @Test
    public void testSubStringsSubtraction(){
        String one = "ccdaabcdbb";
        String []two = {"ab", "cd"};
        Assert.assertEquals(
                SubtractSubStrings.subtract(one, two),
                "cb"
        );
    }

    @Test
    public void testSubStringsSubtractions(){
        String one = "abcd";
        String []two = {"ab", "bcd"};
        Assert.assertEquals(
                SubtractSubStrings.subtract(one, two),
                "cd"
        );
    }

    @Test
    public void testSubStrings(){
        String one = "abcd";
        String []two = {"ab", "cd", "bcd"};
        Assert.assertEquals(
                SubtractSubStrings.subtract(one, two),
                ""
        );
    }
}
package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.LongestValidBraces;

public class LongestValidBracesTests {

    @Test
    public void verifyLongestValidBraces(){
        String [][] braces = {
                {")(()())()", "8"},
                {")(()())))()", "6"},
                {")((((", "0"},
                {"))))", "0"},
                {")((((()", "2"},
        };

        for(String [] d: braces){
            Assert.assertEquals(
                    LongestValidBraces.longestValidBraces(d[0].toCharArray()),
                    Integer.parseInt(d[1])
            );
        }
    }
}
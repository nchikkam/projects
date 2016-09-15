package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.BracesChecker;

public class BracesCheckerTests {

    @Test
    public void testBraces(){
        Assert.assertTrue(
                BracesChecker.check("()")
        );
    }

    @Test
    public void testGoodCases(){
        String [] braces = {
            "",
            "()()()",
            "()[]{}",
            "([{}])()(()())",
            "[[[][]]][[[][][]]]"
        };
        for(String brace: braces) {
            Assert.assertTrue(
                    BracesChecker.check(brace),
                    "Doesn't met expectation: " + brace
            );
        }
    }
    @Test
    public void testVariousCases(){
        String [] braces = {
            "([{}])()(()()",
            "()))",
            "(()()(()",
            "[][][][]][",
            "][[][[]]][]]][[[[]"
        };
        for(String brace: braces) {
            Assert.assertFalse(
                    BracesChecker.check(brace),
                    "Doesn't met expectation: " + brace
            );
        }
    }
}
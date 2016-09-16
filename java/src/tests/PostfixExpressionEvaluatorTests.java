package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.PostfixExpressionEvaluator;

public class PostfixExpressionEvaluatorTests {

    @Test
    public void testBasicExpression(){
        String [][][] data = {
                {{"10", "2", "8", "*", "+", "3", "-"}, {"23"}},
                {{"4", "2", "+", "6", "*"}, {"36"}},
                {{"2","3", "1", "*", "+", "9", "-"}, {"-4"}}

        };
        for (String [][]d: data)
        Assert.assertEquals(
            d[1][0],
            PostfixExpressionEvaluator.eval(d[0])
        );
    }
}
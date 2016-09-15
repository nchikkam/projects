package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.StackWithMin;

public class StackWithMinTests {

    @Test
    public void testMinStackWithElements() throws Exception{
        StackWithMin stack = new StackWithMin();
        for(int i=1; i < 50; i++)
            stack.push(i);

        for(int i = 2; i < 50; i++) {
            Assert.assertEquals(
                    stack.getMin(),
                    1
            );
            stack.pop();
        }
    }

    @Test
    public void testMinStackWithCriteria() throws Exception{
        StackWithMin stack = new StackWithMin();
        for(int i=1; i < 25; i++)
            stack.push(i);

        stack.push(-1);
        for( int i = 25; i < 50; i++)
            stack.push(i);

        for(int i = 50; i > 25; i--) {
            Assert.assertEquals(
                    stack.getMin(),
                    -1
            );
            stack.pop();
        }

        Assert.assertEquals(
                stack.pop(),
                -1
        );
        for(int i = 25; i > 1; i--) {
            Assert.assertEquals(
                    stack.getMin(),
                    1
            );
            stack.pop();
        }

    }
}
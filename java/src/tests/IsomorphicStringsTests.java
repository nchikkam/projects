package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.IsomorphicStrings;

public class IsomorphicStringsTests {

    @Test
    public void testIsomorphism(){
        Assert.assertTrue(
            IsomorphicStrings.verifyIsomorphism(
                    "egg".toCharArray(),
                    "add".toCharArray()
            )
        );
    }
}
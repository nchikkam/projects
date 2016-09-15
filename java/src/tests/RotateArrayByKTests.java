package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.RotateArrayByK;

public class RotateArrayByKTests {

    @Test
    public void testRotationFlipMethod(){
        System.out.println(RotateArrayByK.rotate("abcdefgh".toCharArray(), 6));
        Assert.assertEquals(
                "ghabcdef".toCharArray(),
                RotateArrayByK.rotate("abcdefgh".toCharArray(), 6)
        );
    }
}
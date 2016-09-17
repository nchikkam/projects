package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.KMP;

public class KMPTests {

    @Test
    public void testKMPOLogN(){
        Assert.assertEquals(
            KMP.kmp("concatenate", "cat"),
            3
        );
    }
}
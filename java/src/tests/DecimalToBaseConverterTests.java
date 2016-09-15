package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.DecimalToBaseConverter;

public class DecimalToBaseConverterTests {
    @Test
    public void testHexadecimalConversion(){
        String [][] expected = {
            {"255", "FF"},
            {"15", "F"},
            {"16", "10"},
            {"18", "12"}
        };

        for(String [] input: expected){
            String actual =
                    DecimalToBaseConverter.toHex(new Integer(input[0]).intValue());
            Assert.assertEquals(
                input[1],
                actual,
                "Expected: "+ input[1] + " Actual: " + actual
            );
        }
    }

    @Test
    public void testOctalConversion(){
        String [][] expected = {
            {"255", "377"},
            {"15", "17"},
            {"16", "20"},
            {"18", "22"}
        };

        for(String [] input: expected){
            String actual =
                    DecimalToBaseConverter.toOctal(new Integer(input[0]).intValue());
            Assert.assertEquals(
                    input[1],
                    actual,
                    "Expected: "+ input[1] + " Actual: " + actual
            );
        }
    }

}
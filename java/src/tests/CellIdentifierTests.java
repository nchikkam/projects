package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.CellIdentifier;

public class CellIdentifierTests {
    @Test
    public void testCellToInt(){
        Assert.assertEquals(
                "IV",
                CellIdentifier.toCell(255)
        );
    }

    @Test
    public void testIntToCell(){
        Assert.assertEquals(
                255,
                CellIdentifier.toNumber("IV")
        );
    }
}
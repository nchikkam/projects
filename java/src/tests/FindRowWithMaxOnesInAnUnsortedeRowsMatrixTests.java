package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.FindRowWithMaxOnesInAnUnsortedeRowsMatrix;

public class FindRowWithMaxOnesInAnUnsortedeRowsMatrixTests {

    @Test
    public void testMatrixOne(){
        int [][]a= {
            {0, 0, 0, 1, 1, 1},
            {0, 0, 1, 1, 1, 1},
            {0, 1, 1, 1, 1, 1},
            {0, 0, 0, 0, 1, 1},
            {1, 1, 1, 1, 1, 1}
        };

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_N_2(a),
            4
        );

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_Nlog_N(a),
            4
        );
    }

    @Test
    public void testMatrixTwo(){
        int [][] a = {
            {0, 1, 1, 1},
            {0, 0, 1, 1},
            {1, 1, 1, 1},
            {0, 0, 0, 0}
        };

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_N_2(a),
            2
        );

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_Nlog_N(a),
            2
        );
    }

    @Test
    public void testMatrixThree(){
        int [][] a = {
            {1, 1},
            {1, 0},
            {0, 0},
            {0, 1}
        };

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_N_2(a),
            0
        );

        Assert.assertEquals(
            FindRowWithMaxOnesInAnUnsortedeRowsMatrix.findRowWithMaxOnes_O_Nlog_N(a),
            0
        );
    }
}
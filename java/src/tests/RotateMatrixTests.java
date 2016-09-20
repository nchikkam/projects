package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.RotateMatrix;

public class RotateMatrixTests {

    @Test
    public void testMatrix90DegreesRotation(){
        int [][] matrix = {
                {1,  2,  3,  4},
                {5,  6,  7,  8},
                {9,  10, 11, 12},
                {13, 14, 15, 16}
        };

        int [][]expected = {
            {13, 9,  5, 1},
            {14, 10, 6, 2},
            {15, 11, 7, 3},
            {16, 12, 8, 4}
        };

        RotateMatrix.rotateMatrix(matrix);
        for(int i =0; i < matrix.length; i++){
            for(int j=0; j < matrix[0].length; j++)
                Assert.assertEquals(
                    matrix[i][j],
                    expected[i][j]
                );
        }
    }
}
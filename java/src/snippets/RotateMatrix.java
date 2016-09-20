package snippets;

public class RotateMatrix {

    public static void rotateMatrix(int [][]a){
        int n = a.length; //assuming matrix is a square matrix rows == cols
        // top view outer square
        for(int i=0; i < n/2; i++){
            // elements inside the square.
            for(int j = i; j < n-i-1; j++){
                int temp = a[i][j];
                a[i][j]         = a[n-j-1][i];      // bottom left to top left
                a[n-j-1][i]     = a[n-1-i][n-1-j];  // right bottom to bottom left
                a[n-1-i][n-1-j] = a[j][n-1-i];      // right top to bottom right
                a[j][n-1-i] = temp;                 // initil to right top
            }
        }
    }

    public static void main(String[] args){
        int [][] matrix = {
                {1,  2,  3,  4},
                {5,  6,  7,  8},
                {9,  10, 11, 12},
                {13, 14, 15, 16}
        };

        rotateMatrix(matrix);
        for(int i =0; i < matrix.length; i++){
            for(int j=0; j < matrix[0].length; j++)
                System.out.print(matrix[i][j]+ " ");
            System.out.println();
        }
    }
}
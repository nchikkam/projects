package snippets;

public class BooleanMatrixEditor {

    public static void modifyMatrix(int [][]mat){  // mask all rows and cols to 1's
        int R = mat.length;
        int C = mat[0].length;

        int []row = new int [R];
        int []col = new int [C];

        int i, j;

        // Initialize all values of row[] and col[] as 0
        for (i = 0; i < R; i++)
            row[i] = 0;

        for (i = 0; i < C; i++)
            col[i] = 0;

        for (i = 0; i < R; i++){
            for (j = 0; j < C; j++){
                if (mat[i][j] == 1){
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        /* Modify the input matrix mat[] using the above constructed row[] and
        col[] arrays */
        for (i = 0; i < R; i++){
            for (j = 0; j < C; j++){
                if ( row[i] == 1 || col[j] == 1 )
                    mat[i][j] = 1;
            }
        }
    }

    public static void setZeroes(int[][] matrix) {  // masks to 0's
        boolean firstRowZero = false;
        boolean firstColumnZero = false;

        //set first row and column zero or not
        for(int i=0; i<matrix.length; i++){
            if(matrix[i][0] == 0){
                firstColumnZero = true;
                break;
            }
        }

        for(int i=0; i<matrix[0].length; i++){
            if(matrix[0][i] == 0){
                firstRowZero = true;
                break;
            }
        }

        //mark zeros on first row and column
        for(int i=1; i<matrix.length; i++){
            for(int j=1; j<matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        //use mark to set elements
        for(int i=1; i<matrix.length; i++){
            for(int j=1; j<matrix[0].length; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }

        //set first column and row
        if(firstColumnZero){
            for(int i=0; i<matrix.length; i++)
                matrix[i][0] = 0;
        }

        if(firstRowZero){
            for(int i=0; i<matrix[0].length; i++)
                matrix[0][i] = 0;
        }

    }

    public static void main(String [] args){
        int [][]m = {
            {1, 1, 0, 1, 0},
            {0, 0, 0, 0, 0},
            {0, 1, 0, 0, 0},
            {1, 0, 1, 1, 0}
        };

        modifyMatrix(m);
        for(int i=0; i< m.length; i++){
            for(int j =0; j< m[0].length; j++)
                System.out.print(m[i][j] + " ");
            System.out.println();
        }

        int [][]n = {
                {1, 1, 1, 0},
                {1, 1, 1, 0},
                {1, 1, 0, 0},
                {1, 0, 0, 0}
        };
        setZeroes(n);
        for(int i=0; i< n.length; i++){
            for(int j =0; j< n[0].length; j++)
                System.out.print(n[i][j] + " ");
            System.out.println();
        }
    }
}
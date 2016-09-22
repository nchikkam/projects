package snippets;

public class MaxSubMatrixWithAllOnes {

    public static void findMaxSubMatrix(int [][] M){  // class of DP
        int i,j;
        int R = M.length;
        int C = M[0].length;
        int [][]S = new int [R][C];

        int maximum, i_index_max, j_index_max;
        maximum = S[0][0]; i_index_max = 0; j_index_max = 0;

        /* Set first column of S[][]*/
        for(i = 0; i < R; i++)
            S[i][0] = M[i][0];

        /* Set first row of S[][]*/
        for(j = 0; j < C; j++)
            S[0][j] = M[0][j];

        for(i = 1; i < R; i++){
            for(j = 1; j < C; j++){
                if(M[i][j] == 1)
                    S[i][j] = Math.min(S[i][j-1], Math.min(S[i-1][j], S[i-1][j-1])) + 1;
                else
                    S[i][j] = 0;
            }
        }


        for(i = 0; i < R; i++){
            for(j = 0; j < C; j++){
                if(maximum < S[i][j]){
                    maximum = S[i][j];
                    i_index_max = i;
                    j_index_max = j;
                }
            }
        }

        for(i = i_index_max; i > i_index_max - maximum; i--){
            for(j = j_index_max; j > j_index_max - maximum; j--){
                System.out.print(M[i][j]+ " ");
            }
            System.out.println();
        }
    }

    public static void main(String [] args){
        int [][] a = {
            {0, 1, 1, 0, 1},
            {1, 1, 0, 1, 0},
            {0, 1, 1, 1, 0},
            {1, 1, 1, 1, 0},
            {1, 1, 1, 1, 1},
            {0, 0, 0, 0, 0}
        };

        findMaxSubMatrix(a);
    }
}
package snippets;

public class SortedMatrixSearch {

    public static int [] search_O_N(int [][]a, int k){  //O(N)
        int row = 0;
        int col = a[0].length-1;

        while (row < a.length && col > 0){
            if (a[row][col]>k)
                col--;
            else if (a[row][col]<k)
                row++;
            else
                break;
        }
        if(row < a.length && col >= 0){
            return new int []{row, col};
        }
        return new int[]{-1, -1};
    }

    public static int[] searchMatrix(int[][] matrix, int target) {  //O(logn^2)
        if(matrix==null || matrix.length==0 || matrix[0].length==0)
            return new int[]{-1, -1};

        int m = matrix.length;
        int n = matrix[0].length;

        int start = 0;
        int end = m*n-1;

        while(start<=end){
            int mid=(start+end)/2;
            int midX=mid/n;
            int midY=mid%n;

            if(matrix[midX][midY]==target)
                return new int[]{midX, midY};

            if(matrix[midX][midY]<target){
                start=mid+1;
            }else{
                end=mid-1;
            }
        }

        return new int[]{-1, -1};
    }

    public static void main(String [] args){
        int [][] a = {
                {1, 2, 3, 4 },
                {5, 6, 7, 8 },
                {9,10,11,12 },
                {13,14,15,16},
        };

        int [] r = search_O_N(a, 11);
        System.out.println(r[0]);
        System.out.println(r[1]);

        int [] s = searchMatrix(a, 13);
        System.out.println(s[0]);
        System.out.println(s[1]);
    }
}
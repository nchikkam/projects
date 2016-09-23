package snippets;

public class FindRowWithMaxOnesInAnUnsortedeRowsMatrix {
    /*
        0 1 1 1   -> row is sorted as 0's come first before 1's
        0 0 1 1
        1 1 1 1   -> solution
        0 0 0 0
                  rows are in random order, but each row is sorted. i.e one follows zeros
     */
    public static int findRowWithMaxOnes_O_N_2(int [][]a){ //O(N^2)
        // this logic is good, but its not using the fact that each row is sorted.
        int answer = 0;
        int maxOnes = 0;
        for(int i=0; i< a.length; i++){
            int localCount = 0;
            for(int j=0; j< a[0].length; j++){
                if (a[i][j] == 1)
                    localCount += 1;
            }
            if(maxOnes < localCount){
                maxOnes = localCount;
                answer = i; //i'th row is the answer
            }
        }
        return answer;
    }

    public static int binSearch(int[] a, int lo, int hi){
        // not searching for key, rather for patter ...0[01]1...
        if(hi >= lo){
            int mid = lo + (hi - lo)/2;
            if ( ( mid == 0 || a[mid-1] == 0) && a[mid] == 1 )
                return mid;
            else if (a[mid] == 0 ) // ones on right side
                return binSearch(a, (mid + 1), hi);
            else
                return binSearch(a, lo, (mid -1)); // seach on left
        }
        return -1;
    }

    public static int findRowWithMaxOnes_O_Nlog_N(int [][]a){
        // max no of ones in a row would be the lengthofrow - indexoffirst-1
        int maxOnes = -1;
        int solution = -1;
        for(int i=0; i< a.length; i++){
            // use binary search to find the index of first '1' in row - i
            int pos = binSearch(a[i], 0, a[i].length-1);
            if(pos != -1 && a[i].length-pos > maxOnes){
                solution = i; //ith row
                maxOnes = a[i].length-pos;
            }
        }
        return solution;
    }

    public static void main(String [] args){
        int [][] a = {
            {0, 1, 1, 1},
            {0, 0, 1, 1},
            {1, 1, 1, 1},
            {0, 0, 0, 0}
        };

        System.out.println(findRowWithMaxOnes_O_N_2(a));
        System.out.println(findRowWithMaxOnes_O_Nlog_N(a));
    }
}
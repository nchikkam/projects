package snippets;

public class LongestRepeatedSubString {

    // Compare a[i:] with a[j:] -- strcomp
    public static int comp(String a, int i, int j){
        String one = a.substring(i);
        String two = a.substring(j);
        return one.compareTo(two);
    }

    public static void sortSuffixIndices(String s, int []indices){
        for(int i=0; i < indices.length; i++){
            for (int j = i; j< indices.length; j++){
                if(comp(s, indices[i], indices[j]) > 0){  // ascending order
                    int temp = indices[i];
                    indices[i] = indices[j];
                    indices[j] = temp;
                }
            }
        }
    }

    public static int findMaxPrefixMatch(String a, int i, int j){
        String one = a.substring(i);
        String two = a.substring(j);

        int p=0;
        while(one.charAt(p) == two.charAt(p))
            p++;
        return p;  // max prefix of chars that matched.
    }

    public static int [] lrs(String s){
        /* steps:
           Sort the suffixes with indices.
           Compare consecutive suffixes for max prefix matching.
        */

        int [] indices = new int[s.length()];
        for(int i=0; i < s.length(); i++)
            indices[i] = i;

        sortSuffixIndices(s, indices);
        // now compare consecutive suffixes and the ones that match long width are the ones.
        int max = 0;
        int one=-1, two=-1;
        for(int i=1;i < s.length(); i++){
            int temp = findMaxPrefixMatch(s, indices[i], indices[i-1]);
            if(max < temp) {
                max = temp;
                one = indices[i];
                two = indices[i-1];
            }
        }
        return new int[]{
            one,  // suffix at index i
            two,  // suffix at index j
            max   // max length
        };
    }

    public static void main(String [] args){
        String input = "abbaabc";
        int d [] = lrs(input);
        System.out.println(input.substring(d[0], d[0]+d[2]));
    }
}
package snippets;

public class LongestValidBraces {
    public static int longestValidBraces(char[] braces){
        int opened = 0;
        int validLength = 0;
        int maxLength = -1;
        for(char c: braces){
            if(c == '(')
                opened++;
            else{
                if (opened > 0) {
                    opened--; // pop from stack
                    validLength += 2;
                }else{ // extra closing, reset count
                    opened = 0;
                    validLength = 0;
                }
            }
            if(maxLength < validLength)
                maxLength = validLength;
        }
        return  maxLength;
    }

    public static void main(String [] args){
        System.out.println(longestValidBraces(")(()()))()".toCharArray()));
    }
}
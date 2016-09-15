package snippets;

public class RotateArrayByK {

    public static char[] rotate(char[] s, int k){
        reverse(s, 0, k-1);
        reverse(s, k, s.length-1);
        reverse(s, 0, s.length-1);
        return s;
    }

    public static void reverse(char [] s, int i, int j){
        while(i < j){
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
            ++i;
            --j;
        }
    }
}
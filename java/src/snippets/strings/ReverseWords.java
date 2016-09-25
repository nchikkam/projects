package snippets.strings;

public class ReverseWords {
    public static char[] reverseWords(char[] s){
        int i = 0;
        for (int j = 0; j < s.length; j++){
            if (s[j] == ' '){
                reverseWord(s, i, j-1);
                i = j + 1;
            }
        }

        reverseWord(s, i, s.length-1);
        reverseWord(s, 0, s.length-1);
        return s;
    }

    public static void reverseWord(char [] s, int i, int j){
        while(i < j){
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
            ++i;
            --j;
        }
    }
}
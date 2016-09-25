package snippets.strings;

public class AnagramsChecker {

    public static boolean check(char[] a, char[] b){
        if(a.length != b.length) return false;
        int xor = 0;
        for(int i=0;i < a.length; i++)
            xor ^= ((int)a[i] ^ (int)b[i]);
        return xor == 0;
    }

    public static void main(String [] args){
        System.out.println(check("cat".toCharArray(), "tac".toCharArray()));
        System.out.println(check("anagram".toCharArray(), "nagaram".toCharArray()));
        System.out.println(check("aa".toCharArray(), "aa".toCharArray()));
        System.out.println(check("ab".toCharArray(), "ba".toCharArray()));
    }
}
package snippets.strings;

public class ReverseString {

    public static void swap(char[] a, int i, int j){
        char t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
    public static void reverse(char []s, int left, int right){
        if (left < right) {
            swap(s, left, right);
            reverse(s, ++left, --right);
        }
    }

    public static void reverseIterative(char []s){
        int right = s.length-1;
        int left = 0;
        while(left < right) {
            swap(s, left, right);
            ++left;
            --right;
        }
    }

    public static void main(String [] args){
        char [] s = "bugsbunny".toCharArray();
        reverse(s, 0, s.length-1);
        for (char c: s)
            System.out.print(c);

        System.out.println();
        char [] t = "bugsbunny".toCharArray();
        reverseIterative(t);
        for (char c: t)
            System.out.print(c);
    }
}
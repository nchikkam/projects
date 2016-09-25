package snippets.strings;

import java.util.Stack;

public class RemoveAllAdjacentDuplicates {

    public static String removeAdjacentDuplicatesRecursive(String str, char[] last_removed){
        //O(N) but expensive mutable String!
        if (str.length() <=1) return str;

        if (str.charAt(0) == str.charAt(1)){
            last_removed[0] = str.charAt(0);
            int i = 0;
            while (i < str.length()-1 && str.charAt(i) == str.charAt(i+1))
                i++;
            i++;
            return removeAdjacentDuplicatesRecursive(str.substring(i), last_removed);
        }

        String rem_str = removeAdjacentDuplicatesRecursive(str.substring(1), last_removed);

        if (rem_str.length() > 0 && rem_str.charAt(0) == str.charAt(0)){
            last_removed[0] = str.charAt(0);
            return (rem_str.substring(1));
        }

        if (rem_str.length() == 0 && last_removed[0] == str.charAt(0))
            return rem_str;

        rem_str = str.charAt(0)+ rem_str;
        return rem_str;
    }

    public static String remove(String str)
    {
        char []last_removed = new char [1];
        return removeAdjacentDuplicatesRecursive(str, last_removed);
    }

    public static void main(String [] args){
        System.out.println(remove("acaaabbbacdddd"));  //acac
        System.out.println(remove("qpaaaaadaaaaadprq"));  //qrq
        System.out.println(remove("aaaaaaaaaa"));
        System.out.println(remove("aaaaaaaaa"));

        System.out.println(remove("azxxxzy"));
        System.out.println(remove("azxxxxzy"));
    }
}
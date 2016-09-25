package snippets.strings;

import java.util.Hashtable;

public class FirstNonRepeatingChar {

    public static int firstNonRepeatingChar(char[] s) {
        Hashtable<Character, Integer> map =
                new Hashtable<Character, Integer>();

        for (char c : s)
            map.put(c, map.getOrDefault(c, new Integer(0)) + 1);

        for (int i=0; i < s.length; i++)
            if (map.get(s[i]) == 1)
                return i;
        return -1;
    }

    public static void main(String [] args){
        char[] s = "concatenation".toCharArray();
        System.out.println(firstNonRepeatingChar(s));
    }
}
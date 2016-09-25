package snippets.strings;

import java.util.Hashtable;

public class MaskChars {

    public static String maskCharacters(char[] s, char[] t){
        Hashtable<Character, Integer> map =
                new Hashtable<Character, Integer>();

        for(char c: t)
            map.put(c, map.getOrDefault(c, new Integer(0))+1);

        StringBuffer sb = new StringBuffer();
        for(char c: s)
            if(!map.containsKey(c))
                sb.append(c);

        return sb.toString();
    }

    public static void main(String [] args){
        String ret = maskCharacters("concatenation".toCharArray(), "cat".toCharArray());
        System.out.println(ret);
    }
}
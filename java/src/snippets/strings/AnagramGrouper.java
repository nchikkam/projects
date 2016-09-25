package snippets.strings;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Hashtable;

public class AnagramGrouper {

    public static String sort(String s){
        char [] c = s.toCharArray();
        Arrays.sort(c);  //another way is summing chars to int
        return new String(c);
    }

    public static Hashtable<String, ArrayList<String>> groupAnagrams(String[] strs){
        Hashtable<String, ArrayList<String>> ret =
                new Hashtable<String, ArrayList<String>>();

        for(String s: strs){
            String signature = sort(s);

            ArrayList<String> list = null;
            if ( ret.containsKey(signature) )
                list = ret.get(signature);
            else{
                list = new ArrayList<String>();
                ret.put(signature, list);
            }
            list.add(s);
        }
        return ret;
    }

    public static long getSignature(String s){
        char []c = s.toCharArray();
        long ret = 0;
        for(char d: c){
            ret += (int)d;
        }
        return ret;
    }
    public static int groupAnagramsWithINTSignature(String[] strs){
        Hashtable<Long, ArrayList<String>> ret =
                new Hashtable<Long, ArrayList<String>>();

        for(String s: strs){
            long signature = getSignature(s);

            ArrayList<String> list = null;
            if ( ret.containsKey(signature) )
                list = ret.get(signature);
            else{
                list = new ArrayList<String>();
                ret.put(signature, list);
            }
            list.add(s);
        }
        return ret.size();
    }
}
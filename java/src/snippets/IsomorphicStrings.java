package snippets;

import java.util.Hashtable;

public class IsomorphicStrings {

    public static boolean verifyIsomorphism(char[]a, char[] b){
        // two strings are said to be isomorphic when each character
        // in the strings associates to the same character in other
        // eg: egg -> add are isomorphic as e -> a, g->d

        if(a.length==0||b.length==0)
            return false;

        Hashtable<Character, Character> map =
                new Hashtable<Character, Character>();
        for(int i =0; i < a.length; i++) {
            if (map.containsKey(a[i])){
                if (map.get(a[i])!=b[i])
                    return false;  // char in second doesn't correspond
            }else{
                if(map.containsValue(b[i]))  // char in b at i already mapped
                    return false;
                map.put(a[i], b[i]); // create association
            }
        }
        return true;
    }

    public static void main(String[] args){

    }
}
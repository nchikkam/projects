package snippets;

import java.util.Hashtable;
import java.util.Stack;

public class BracesChecker {

    public static boolean comp(char c, Stack st){
        if (st.empty()) return false;  // stack empty, ]]]] case

        Hashtable<String,String> lookup =
                new Hashtable<String, String>(){
            {
                put(")", "(");
                put("]", "[");
                put("}", "{");
            }
        };

        return st.pop().equals(lookup.get(""+c));  // top element must match lookup
    }

    public static boolean check(String braces){
        Stack<String> st = new Stack<>();
        char[] chars = braces.toCharArray();

        for( char c: chars){
            if (c == '(' || c == '['||c =='{')
                st.push(""+c);
            else if (comp(c, st) == false) // if stack match failed, return false
                return false;
            // ignore other chars
        }

        return st.empty();
    }
}
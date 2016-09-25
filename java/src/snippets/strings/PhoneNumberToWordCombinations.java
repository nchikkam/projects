package snippets.strings;

import java.util.Hashtable;

public class PhoneNumberToWordCombinations {
    public static Hashtable<Integer, Character[]>  map = new Hashtable<Integer, Character[]>(){
        {
            put(0, new Character[]{'0'});
            put(1, new Character[]{'1'});
            put(2, new Character[]{'a', 'b', 'c'});
            put(3, new Character[]{'d', 'e', 'f'});
            put(4, new Character[]{'g', 'h', 'i'});
            put(5, new Character[]{'j', 'k', 'l'});
            put(6, new Character[]{'m', 'n', 'o'});
            put(7, new Character[]{'p', 'q', 'r', 's'});
            put(8, new Character[]{'t', 'u', 'v'});
            put(9, new Character[]{'w', 'x', 'y', 'z'});
        }
    };

    public static void generateWordsFromPhoneNumber(char [] digits, int depth, StringBuffer word){
        if (depth == digits.length){
            System.out.println(word);
        }else{
            for(char c: map.get(Integer.parseInt(""+digits[depth]))){
                word.append(c);
                generateWordsFromPhoneNumber(digits, depth + 1, word);
                word.deleteCharAt(word.length()-1);
            }
        }
    }

    public static void main(String [] args){
        String s = "32";
        generateWordsFromPhoneNumber(s.toCharArray(), 0, new StringBuffer());
    }
}
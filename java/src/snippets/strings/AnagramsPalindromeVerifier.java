package snippets.strings;

import java.util.Hashtable;

public class AnagramsPalindromeVerifier {
    /*
    Palindrome has a property, if length is even, every char must appear twice
    if odd in length, ignore the middle char
   */
    public static boolean isPalindrome(char []s){
        // Create a count array and initialize all values as 0
        Hashtable<Character, Integer> map = new Hashtable<Character, Integer>();

        for (int i = 0; i < s.length;  i++) {
            if (map.containsKey(s[i])) {
                Integer count = map.get(s[i]);
                count += 1;
                map.put(s[i], count);
            } else
                map.put(s[i], 1);
        }

        int oddChars = 0;
        for( Character k: map.keySet()){
            if(map.get(k) % 2 == 1) // odd
                oddChars++;
        }
        // Return true if odd count is 0 or 1, otherwise false
        return (oddChars <= 1);// if there is odd occurance it must be one and in the middle
    }

    public static void main(String [] args){
        System.out.println(isPalindrome("able was I able was".toCharArray()));
        System.out.println(isPalindrome("able was I able wa".toCharArray()));
    }
}
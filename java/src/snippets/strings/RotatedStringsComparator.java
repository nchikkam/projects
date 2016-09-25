package snippets.strings;

public class RotatedStringsComparator {

    public static boolean checkRotation(String s, String t){
        if(s.length() != t.length())
            return false;

        return (s+s).indexOf(t) != -1;
    }

    public static void main(String [] args){
        System.out.println(checkRotation("1234", "3412"));
        System.out.println(checkRotation("1234", "4123"));
        System.out.println(checkRotation("1234", "1234"));
        System.out.println(checkRotation("1234", "2341"));
    }
}
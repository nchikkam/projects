package snippets.strings;

public class ReplaceSpaceWithGivenString {

    public static char[] replace(char[] str, char[] pattern) {
        StringBuffer sb = new StringBuffer();  //sb is better than immutable Strings
        for(char c: str){
            if (c == ' ')
                sb.append(pattern);
            else
                sb.append(c);
        }
        return new String(sb).toCharArray();
    }

    public static void main(String[] args){
        System.out.println(replace("con cat enation".toCharArray(), "dog".toCharArray()));
    }
}
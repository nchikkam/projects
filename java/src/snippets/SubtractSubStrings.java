package snippets;

public class SubtractSubStrings {

    public static String subtract(String one, String []two){
        while(true){
            int index = -1;
            int pos = -1;
            for(int i = 0; i < two.length; i++){
                index = one.indexOf(two[i]);
                if (index != -1){
                    pos = i;
                    break;
                }
            }

            if( index != -1 ){
                int end = two[pos].length();
                one = one.substring(0, index)+ one.substring(index+end);
            }else
                break;
        }
        return one;
    }

    public static void main(String [] args){
        String one = "ccdaabcdbb";
        String []two = {"ab", "cd"};
        System.out.println(subtract(one, two));
    }
}
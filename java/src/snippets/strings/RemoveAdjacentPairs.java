package snippets.strings;

import java.util.Stack;

public class RemoveAdjacentPairs {

    public static void removeAdjacentPair(char[] str){
        int len = str.length;
        int i,j=0;
        for(i=1; i < len; i++){
            while((str[i]==str[j]) && (j >= 0)){
                i++;
                j--;
            }
            str[++j] = str[i];
        }
        for(i=0; i<= j; i++)
            System.out.print(str[i]);
        System.out.println();
    }

    static StringBuffer eliminateAdjacentPair(StringBuffer strBuf){
        for(int i = 0; i < strBuf.length()-1;){
            if(strBuf.charAt(i) == strBuf.charAt(i+1)){
                strBuf.delete(i, i+2);
                i = i-1;
                continue;
            }
            i++;
        }
        return strBuf;
    }

    /*public static char [] removeDup(char [] str, int n) {
        int i, k=0;
        int len= str.length;
        for(i=1; i< len; i++){
            if(str[i-1]!=str[i])
                str[k++]=str[i-1];
            else  {
                while(i< str.length && str[i-1]==str[i])
                    i++;
            }
        }
        str[k++]=str[i-1];
        str[k]='\0';

        if(k != n)
            removeDup(str, k);	// Shlemial Painter's Algorithm

        return str;
    }*/

    public static String removeAdjacentDulicatesUsingStack(char []str){
        // Doesn't work for adjacent cases
        Stack<Character> stack = new Stack<Character>();
        stack.push(str[0]);

        int count = 1;

        for(int i=1; i < str.length; i++){
            if (! stack.empty() && stack.peek() == str[i]){
                stack.pop();
                count -= 1;
            }else{
                stack.push(str[i]);
                count += 1;
            }
        }

        char ret[] = new char[count];
        count -= 1;
        while(!stack.empty()){
            ret[count] = stack.pop();
            count -= 1;
        }

        return new String(ret);
    }



    public static void main(String[] args){
        //char []d = "acaaabbbacdddd".toCharArray();
        char [] d = "RGBBGBGR".toCharArray();
        removeAdjacentPair(d);

        StringBuffer sb = new StringBuffer("RGBBGBGR");
        System.out.println(eliminateAdjacentPair(sb));

        System.out.println(removeAdjacentDulicatesUsingStack("RGBBGBGR".toCharArray()));
     }
}
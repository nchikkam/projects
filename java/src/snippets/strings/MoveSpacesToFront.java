package snippets.strings;

public class MoveSpacesToFront {

    public static void moveSpacesToFront(char[] a){
        int n = a.length-1;
        int count = n;

        for(int i=n;i>=0;i--){
            if(a[i] != ' ')
                a[count--] = a[i];
        }

        while(count>=0)
            a[count--] = ' ';
    }

    public static void main(String [] args){
        char [] s = "This is an Example.".toCharArray();
        moveSpacesToFront(s);
        System.out.println(s);
    }
}
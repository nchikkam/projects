package snippets;

public class Permutations {

    public static void swap(char[] a, int i, int j){
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void permutations(char [] a, int pos){
        if (pos == a.length)
            System.out.println(new String(a));
        else {
            for (int i = pos; i < a.length; i++) {
                swap(a, pos, i);
                permutations(a, pos + 1);
                swap(a, pos, i);
            }
        }
    }

    public static void main(String[] args){
        char [] c = {'a', 'b', 'c', 'd'};
        permutations(c, 0);
    }
}
package snippets;

public class UnionOfTwoArrays {
    public static void union(int a[], int b[]){
        int i = 0, j = 0;
        while(i < a.length && j < b.length){
            if(a[i] < b[j])
                System.out.print(a[i++]+ " ");
            else if(b[j] < a[i])
                System.out.print(b[j++]);
            else{
                System.out.print(a[i]);
                i++; j++;
            }
        }
        while(i < a.length)
            System.out.print(a[i++]+ " ");
        while(j < b.length)
            System.out.print(b[j++]+ " ");
    }

    public static void main(String [] args){
        int a[] = {1, 2, 3, 4, 5 };
        int b[] = {6, 7, 8, 9, 10};

        union(a, b);
    }
}
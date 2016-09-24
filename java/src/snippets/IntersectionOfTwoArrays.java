package snippets;

public class IntersectionOfTwoArrays {
    public static void intersection(int a[], int b[]){
        int i = 0, j = 0;
        while(i < a.length && j < b.length){
            if(a[i] < b[j])
                i++;
            else if(b[j] < a[i])
                j++;
            else{
                System.out.print(a[i]+ " ");
                i++; j++;
            }
        }
    }

    public static void main(String [] args){
        int a[] = {1, 2, 3, 4, 5 };
        int b[] = {2, 5, 8, 9, 10};

        intersection(a, b);
    }
}
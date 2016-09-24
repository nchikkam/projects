package snippets;

public class MoveEvenToLeftOddToRight {

    public static void swap(int [] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    public static void moveEvenToLeftOddToRight(int a[]){
        int odd     = 1;
        int even    = 0;
        while (true){
            while (even < a.length && a[even]%2 == 0) even += 2;
            while (odd < a.length && a[odd]%2 == 1)   odd += 2;
            if (even < a.length && odd < a.length) swap (a, even, odd);
            else break;
        }
    }

    public static void main(String [] args){
        int a[] = {12, 34, 45, 9, 8, 90, 3};
        moveEvenToLeftOddToRight(a);
        for(int v: a)
            System.out.print(v + " ");
        System.out.println();
    }
}
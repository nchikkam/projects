package snippets;

public class EvenToEvenOddToOddArrange {

    public static void moveEvenToEvenIndexOddToOddIndex(int arr[]) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            // stop at even number
            while (arr[left] % 2 == 0 && left < right)
                left++;

            // stop at odd number
            while (arr[right] % 2 == 1 && left < right)
                right--;

            if (left < right) { // swap if haven't crossed
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
    }

    public static void main(String [] args){
        int a[] = {12, 34, 45, 9, 8, 90, 3};
        moveEvenToEvenIndexOddToOddIndex(a);
        for(int v: a)
            System.out.print(v + " ");
        System.out.println();
    }
}
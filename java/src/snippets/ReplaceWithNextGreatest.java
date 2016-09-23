package snippets;

public class ReplaceWithNextGreatest {

    /*
        replace every element with the next greatest element on the right side
        in the array. Replace last element with 0 as there no element on the
        right side of it
     */
    public static void replaceWithNextGreatest(int a[]){
        int maximum =  a[a.length-1];
        a[a.length-1] = 0; // last element is always replace with zero

        // Replace all other elements with the next greatest
        for(int i = a.length-2; i >= 0; i--){
            int temp = a[i];
            a[i] = maximum;

            // Update the greatest element, if needed
            if(maximum < temp)
                maximum = temp;
        }
    }

    public static void main(String [] args){
        int a[] = {6, 7, 4, 3, 5, 2};
        replaceWithNextGreatest(a);
        for(int v: a)
            System.out.print(v+ " ");
        System.out.println();
    }
}
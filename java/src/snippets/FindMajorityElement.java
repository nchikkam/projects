package snippets;

public class FindMajorityElement {

    // Moore’s Voting Algorithm
    /*
        findCandidate(a[], size)
        1.  Initialize index and count of majority element
             maj_index = 0, count = 1
        2.  Loop for i = 1 to size – 1
            (a) If a[maj_index] == a[i]
                  count++
            (b) Else
                count--;
            (c) If count == 0
                  maj_index = i;
                  count = 1
        3.  Return a[maj_index]
     */
    public static boolean majorityExists(int []a){
        int maj_index = 0, count = 1;
        for (int i = 1; i < a.length; i++){
            if (a[maj_index] == a[i]) count++;
            else count--;
            if (count == 0){
                maj_index = i;
                count = 1;
            }
        }
        int f = a[maj_index];

        for (int i = 0; i < a.length; i++)
            if (a[i] == f)
                count++;

        if (count > a.length/ 2) {
            System.out.println(f);
            return true;
        }
        else return false;
    }

    public static void main(String [] args){
        int [] a = {1, 3, 3, 1, 2};
        System.out.println(majorityExists(a));

        int [] b = {3, 3, 4, 2, 4, 4, 2, 4, 4};
        System.out.println(majorityExists(b));
    }
}
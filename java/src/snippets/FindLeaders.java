package snippets;

public class FindLeaders {

    // an element is a leader if its bigger than all its right elements
    // right most element is always leader
    public static void findLeaders(int [] a){
        int lead =  a[a.length-1];
        int i;

        System.out.println(lead);
        for(i = a.length-2; i >= 0; i--){
            if(lead < a[i]){
                lead = a[i];
                System.out.println(lead);
            }
        }
    }

    public static void main(String [] args){
        int [] a = {6, 7, 4, 3, 5, 2};
        findLeaders(a);
    }
}
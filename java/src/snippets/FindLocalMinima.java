package snippets;

public class FindLocalMinima {

    // key is any local minima ... thats what makes bin search useful here.
    public static int findLocalMinima(int[] a, int start, int end){
        int mid = (start + end)/2;
        if (mid == a.length-1 || mid == 0) return mid;
        if(a[mid-1]>=a[mid] && a[mid]<= a[mid+1])
            return mid;
        else if(a[mid-1]<a[mid])
            return findLocalMinima(a, start, mid-1);
        else if(a[mid]>a[mid+1])
            return findLocalMinima(a, mid+1, end);
        return -1;
    }

    public static void main(String[] args){
        int [] a = {1, 2, 6, 5, 3, 7, 4};
        System.out.println(findLocalMinima(a, 0, a.length-1));
    }
}
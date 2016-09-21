package snippets;

public class PeakElement {

    // the key is just any element which is peak is solution.
    public static int peak(int []a, int start, int end){  // bin search works !
        int mid = (start + end)/2;
        if (mid == a.length-1 || mid == 0) return mid;
        if(a[mid-1]<=a[mid] && a[mid]>= a[mid+1])
            return mid;
        else if(a[mid-1]>a[mid])
            return peak(a, start, mid-1);
        else if(a[mid]<a[mid+1])
            return peak(a, mid+1, end);
        return -1;
    }

    public static void main(String[] args){
        int [] a = {1, 2, 6, 5, 3, 7, 4};
        System.out.println(peak(a, 0, a.length));
    }
}

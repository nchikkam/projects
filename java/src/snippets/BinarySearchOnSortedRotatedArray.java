package snippets;

public class BinarySearchOnSortedRotatedArray {

    public static int searchInShiftedArr(int[] arr, int key) {
        if (arr == null || arr.length == 0) {
            return -1;
        }
        int low = 0;
        int high = arr.length - 1;
        int mid; // declared outside loop to avoid constant memory allocation for this variable
        while (low <= high) {
            mid = (low + high) >>> 1; // same as "(low + high) / 2", but avoid negative overflow
            if (arr[mid] == key) {    // and should be faster than "low + (high - low)/2"
                return mid;
            }
            if (arr[low] <= arr[mid]) { // means left half of the array is sorted
                if (arr[low] <= key && key < arr[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else { // means right half of the array is sorted
                if (arr[mid] < key && key <= arr[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args){
        int a[] = {4, 5, 6, 7, 1, 2, 3};
        System.out.println(searchInShiftedArr(a, 6));
    }
}
package snippets;

import java.util.HashMap;
import java.util.Arrays;

public class ComplementaryPairs{

	// Classic swap method to exchange vaules of two entries in an array
	// there are solutions with out using third variable with XOR and so
	// on. But for the readability this approach was chosen.
	private void swap(int []a, int i, int j){
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}

	/*
		There are other solutions to this that use O(N) space and O(N) time
		complexity, which are commented for idea sharing.

		For smaller amount of data in the array, its works, but
		in efficient when the data is more. Below algorithm uses Quick Sort
		that sorts elements in O(Nlogn) time first and then it uses below
		approach to find the pairs:
			keeps a left pointer that traverses forward from index 0
			and a right pointer that traverses backwards from last index.
			each time the sum formed by the values at left and right pointers
			were compared against given K, the poiners are tuned as per the
			comparision so as to find the pairs.


	 */
	public boolean findComplimentaryPair_O_NlogN(int []a, int k, int[] basket){
		QuickSort.qSort(a, 0, a.length-1);
		int i = 0;		//left pointer
		int j = a.length - 1;  // right pointer

		while( i <= j){
		     int s = a[i] + a[j];
		     if(s < k){
		        ++i;
		     }else if( s > k ){
		        --j;
		     }else{
		        basket[0] = i;
		        basket[1] = j;
		        return true;
		     }
		 }
		 return false;
	}


	public static void main(String [] args){

		ComplementaryPairs obj = new ComplementaryPairs();

		int [] basket = {-1, -1};
		int []input = {30, 1, 2, 3, 4, 5,28};
		int k = 58;

		//if (obj.findComplimentaryPairO_N2(input, 60, basket)){
		if (obj.findComplimentaryPair_O_NlogN(input, k, basket)){
			System.out.println("ComplementaryPair:{" +input[basket[0]] + ", " + input[basket[1]]+"}");
		}else{
			System.out.println("ComplementaryPair Doesn't exist");
		}
	}

	/*
	//Other Alternatives for Shring work:
	public boolean findComplimentaryPairO_N2(int []a, int k, int[]basket){

		for(int i =0; i < a.length; i++){   		//  N times
			for (int j=i+1; j < a.length; j++){ 	//  N times = O(N^2)
				if(a[i]+a[j] == k){
					basket[0] = i;
					basket[1] = j;
					return true;
				}
			}
		}
		return false;
	}

	public boolean findComplimentaryPairO_N(int []a, int k, int[]basket){
		// idea is to keep the K-i in the map, on one scan we look in this
		// map, if ith element is found in the map, it means we found the
		// pair.
		HashMap<Integer, Integer> lookup = new HashMap();		// O(N) Space

		for(int i =0; i < a.length; i++){  			// O(N) time
			Integer elem = new Integer(a[i]);
			Integer diff = new Integer(k-a[i]);

			if (lookup.containsKey(elem)){			//O(1) lookup in map
				basket[0] = i;
				basket[1] = lookup.get(elem).intValue();
				return true;
			}else{
				lookup.put(diff, new Integer(i));
			}
		}
		return false;
	}
	*/
}
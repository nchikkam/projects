package snippets;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombinationSum {
    /*
        Elements in a combination (a1, a2,…, ak) must be in non-descending order.(ie, a1 ≤ a2 ≤.. ≤ ak).
        The solution set must not contain duplicate combinations.
     */

    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();

        backTrack(result, list, candidates, target, 0);

        return result;
    }

    private static void backTrack(List<List<Integer>> result,
                           List<Integer> list, int[] candidates, int target,
                           int position) {

        int sum = 0;
        for (int x: list) {
            sum += x;
        }

        if (sum == target) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        if (sum < target)
        {
            for (int i = position; i < candidates.length; i++)
            {
                if(position != i
                        && candidates[i] == candidates[i-1])
                {
                    continue;
                }
                list.add(candidates[i]);
                backTrack(result, list, candidates, target, i+1);
                list.remove(list.size() - 1);
            }
        }
    }

    public static void main(String [] args){
        int [] candidates = {10, 1, 2, 7, 6, 1, 5};

        List<List<Integer>> sets = combinationSum(candidates, 8);
        for( List<Integer> l: sets){
            for (Integer i: l){
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}
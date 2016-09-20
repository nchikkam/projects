package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.CombinationSum;

import java.util.List;

public class CombinationSumTests {

    @Test
    public void test() {
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};

        List<List<Integer>> sets = CombinationSum.combinationSum(candidates, 8);
        Assert.assertEquals(
                sets.size(),
                4
        );

        /*for( List<Integer> l: sets){
            for (Integer i: l){
                System.out.print(i + " ");
            }
            System.out.println();
        }}*/
    }
}

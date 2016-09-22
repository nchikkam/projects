package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.LargestSubArrayWithEqual01s;

public class LargestSubArrayWithEqual01sTests {
    @Test
    public void testBasicCases() {
        int[] a = {1, 0, 1, 1, 1, 0, 0, 0, 1};
        int[] data1 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_3(a);
        int[] data2 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_2(a);
        int[] data3 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits(a);

        Assert.assertTrue(
                data1[0] == 8 && data1[1] == 0 && data1[2] == 7
        );
        Assert.assertTrue(
                data2[0] == 8 && data2[1] == 0 && data2[2] == 7
        );
        Assert.assertTrue(
                data3[0] == 8 && data3[1] == 0 && data3[2] == 7
        );
    }

    @Test
    public void testDataSetTwo() {
        int[] a = {1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1};
        int[] data1 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_3(a);
        int[] data2 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_2(a);
        int[] data3 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits(a);

        Assert.assertTrue(
                data1[0] == 4 && data1[1] == 3 && data1[2] == 6
        );
        Assert.assertTrue(
                data2[0] == 4 && data2[1] == 3 && data2[2] == 6
        );
        Assert.assertTrue(
                data3[0] == 4 && data3[1] == 3 && data3[2] == 6
        );
    }

    @Test
    public void testDataSetThree(){
        int a[] = {1, 1, 1, 1, 1, 1 ,1, 0 ,0, 0 ,0, 1, 1 ,1 ,1, 1 ,1};
        int[] data1 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_3(a);
        int[] data2 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_2(a);
        int[] data3 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits(a);

        Assert.assertTrue(
                data1[0] == 8 && data1[1] == 3 && data1[2] == 10
        );
        Assert.assertTrue(
                data2[0] == 8 && data2[1] == 3 && data2[2] == 10
        );
        Assert.assertTrue(
                data3[0] == 8 && data3[1] == 3 && data3[2] == 10
        );
    }

    @Test
    public void testDataSetFour(){
        int a[] = {0, 1};
        int[] data1 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_3(a);
        int[] data2 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_2(a);
        int[] data3 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits(a);

        Assert.assertTrue(
                data1[0] == 2 && data1[1] == 0 && data1[2] == 1
        );
        Assert.assertTrue(
                data2[0] == 2 && data2[1] == 0 && data2[2] == 1
        );
        Assert.assertTrue(
                data3[0] == 2 && data3[1] == 0 && data3[2] == 1
        );
    }

    @Test
    public void testDataSetFive(){
        int a[] = {1};
        int[] data1 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_3(a);
        int[] data2 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits_O_N_2(a);
        int[] data3 = LargestSubArrayWithEqual01s.largestSubArrayWithEqualBits(a);

        Assert.assertTrue(
                data1[0] == -1 && data1[1] == -1 && data1[2] == -1
        );
        Assert.assertTrue(
                data2[0] == -1 && data2[1] == -1 && data2[2] == -1
        );
        Assert.assertTrue(
                data3[0] == -1 && data3[1] == -1 && data3[2] == -1
        );
    }
}
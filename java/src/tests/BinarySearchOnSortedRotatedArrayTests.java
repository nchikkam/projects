package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.BinarySearchOnSortedRotatedArray;

public class BinarySearchOnSortedRotatedArrayTests {
    @Test
    public void test(){
        int a[] = {4, 5, 6, 7, 1, 2, 3};
        int [][]expected = {
            // position,                                                   Key
                {0, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 4)},
                {1, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 5)},
                {2, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 6)},
                {3, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 7)},
                {4, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 1)},
                {5, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 2)},
                {6, BinarySearchOnSortedRotatedArray.searchInShiftedArr(a, 3)}
        };
        for(int [] data: expected){
            Assert.assertEquals(
                    data[1],
                    data[0]
            );
        }
    }
}
package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.KthElementFinder;

public class KthElementFinderTests {

    @Test
    public void testKthElement(){
        int a[] = {2, 4, 1, 6, 7, 9, 8, 5, 3};

        for(int i =1; i< a.length; i++){
            Assert.assertEquals(
                i,
                KthElementFinder.kthElement(a, i-1)
            );
        }
    }

    @Test
    public void testKthElementSingleElementArray(){
        int a[] = {2};

        int [] expected = {2};
        for(int i =1; i< a.length; i++){
            Assert.assertEquals(
                    i,
                    KthElementFinder.kthElement(a, i-1)
            );
        }
    }

    public void testKthElementRepeatedElements(){
        int a[] = {2, 4, 1, 6, 1, 9, 1, 5, 1};

        int []expected = {1, 1, 1, 1, 2, 4, 5, 6, 9};
        for(int i =1; i< a.length; i++){
            Assert.assertEquals(
                    expected[i],
                    KthElementFinder.kthElement(a, i-1)
            );
        }
    }
}
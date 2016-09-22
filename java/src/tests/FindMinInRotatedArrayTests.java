package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.FindMinInRotatedArray;

public class FindMinInRotatedArrayTests {
    @Test
    public void test() {
        int a[] = {8, 9, 1, 2, 3, 4, 5, 6, 7};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );
    }

    @Test
    public void testOne(){
        int a[] =  {5, 6, 1, 2, 3, 4};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

    }

    @Test
    public void test2(){
        int a[] =  {1, 2, 3, 4};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

    }

    @Test
    public void test3(){
        int a[] =  {1};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );
        a =  new int[]{1, 2};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

        a =  new int []{2, 1};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

        a =  new int [] {5, 6, 7, 1, 2, 3, 4};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

        a = new int[]{1, 2, 3, 4, 5, 6, 7};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

        a = new int[] {2, 3, 4, 5, 6, 7, 8, 1};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );

        a = new int[] {3, 4, 5, 1, 2};
        Assert.assertEquals(
                FindMinInRotatedArray.findMin(a, 0, a.length - 1),
                1
        );
    }
}
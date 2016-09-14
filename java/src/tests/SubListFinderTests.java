package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.SubListFinder;

import java.util.Hashtable;

public class SubListFinderTests {

    @Test
    public void testEmptyList(){
        SubListFinder subject = new SubListFinder();
        SubListFinder.LinkedList first = subject.new LinkedList();

        first.data = "a";

        Assert.assertEquals(
            subject.findSubList(first, null),
            -1
        );
    }

    @Test
    public void testSubListExists(){
        SubListFinder subject = new SubListFinder();
        SubListFinder.LinkedList first = subject.new LinkedList();
        SubListFinder.LinkedList second = subject.new LinkedList();
        SubListFinder.LinkedList third = subject.new LinkedList();

        first.data = "a";
        second.data = "b";
        third.data = "c";

        first.next = second;
        second.next = third;

        Hashtable<Integer, SubListFinder.LinkedList> testData =
                new Hashtable<Integer, SubListFinder.LinkedList>(){
            {
                put(new Integer(0), first);
                put(new Integer(1), second);
                put(new Integer(2), third);
            }
        };

        for(Integer expected: testData.keySet()){
            Assert.assertEquals(
                subject.findSubList(first, testData.get(expected)),
                expected.intValue()
            );
        }
    }
}
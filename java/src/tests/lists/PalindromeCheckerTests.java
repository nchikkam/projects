package tests.lists;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.lists.PalindromeChecker;

public class PalindromeCheckerTests {

    public PalindromeChecker.Node createDataCaseOne(){
        char [] data = "aba".toCharArray();
        PalindromeChecker.Node head = new PalindromeChecker.Node('a');
        PalindromeChecker.Node temp = head;
        for(int i=1;i< data.length; i++) {
            temp.next = new PalindromeChecker.Node(data[i]);
            temp = temp.next;
        }
        return head;
    }
    @Test
    public void test3LettersPalindrome(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(createDataCaseOne()));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(createDataCaseOne()));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(createDataCaseOne()));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(createDataCaseOne()));
    }

    @Test
    public void test1LetterPalindrome(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(new PalindromeChecker.Node('a')));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(new PalindromeChecker.Node('a')));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(new PalindromeChecker.Node('a')));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(new PalindromeChecker.Node('a')));
    }

    @Test
    public void test0LetterPalindrome(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(null));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(null));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(null));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(null));
    }

    public PalindromeChecker.Node createData(){
        char [] data = "aa".toCharArray();
        PalindromeChecker.Node head = new PalindromeChecker.Node('a');
        PalindromeChecker.Node temp = head;
        for(int i=1;i< data.length; i++) {
            temp.next = new PalindromeChecker.Node(data[i]);
            temp = temp.next;
        }
        return head;
    }
    @Test
    public void testEvenLenghtList(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(createData()));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(createData()));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(createData()));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(createData()));
    }

    public PalindromeChecker.Node data(){
        char [] data = "aaaa".toCharArray();
        PalindromeChecker.Node head = new PalindromeChecker.Node('a');
        PalindromeChecker.Node temp = head;
        for(int i=1;i< data.length; i++) {
            temp.next = new PalindromeChecker.Node(data[i]);
            temp = temp.next;
        }
        return head;
    }
    @Test
    public void testEvenLengthLists(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(data()));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(data()));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(data()));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(data()));
    }

    public PalindromeChecker.Node dataSet(String data){
        char [] d = data.toCharArray();
        PalindromeChecker.Node head = new PalindromeChecker.Node('a');
        PalindromeChecker.Node temp = head;
        for(int i=1;i< d.length; i++) {
            temp.next = new PalindromeChecker.Node(d[i]);
            temp = temp.next;
        }
        return head;
    }
    @Test
    public void testEvenLengthsList(){
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(dataSet("aaaabbccbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(dataSet("aaaabbccbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(dataSet("aaaabbccbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(dataSet("aaaabbccbbaaaa")));

        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(dataSet("aaaabbcbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(dataSet("aaaabbcbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(dataSet("aaaabbcbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(dataSet("aaaabbcbbaaaa")));

        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFullList(dataSet("aaaabbbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeSecondHalfReverseList(dataSet("aaaabbbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeReverseFirstHalf(dataSet("aaaabbbbaaaa")));
        Assert.assertTrue(PalindromeChecker.isPalindromeUsingStack(dataSet("aaaabbbbaaaa")));
    }
}
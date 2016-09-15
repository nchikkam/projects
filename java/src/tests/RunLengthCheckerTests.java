package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.RunLengthChecker;

public class RunLengthCheckerTests {

    @Test
    public void testRunLengthEncoding(){
        String [][] data = {
            {"1", "11"},
            {"11", "21"},
            {"21", "1211"},
            {"1211", "111221"},
            {"111221", "312211"},
            {"312211", "13112221"}
        };
        for(String [] d: data){
            Assert.assertEquals(
                RunLengthChecker.RLE(d[0]),
                d[1]
            );
        }
    }

    @Test
    public void testRunLengthDecoding(){
        String [][] data = {
            {"11", "1"},
            {"21", "11"},
            {"1211", "21"},
            {"111221", "1211"},
            {"312211", "111221"},
            {"13112221", "312211"}
        };
        for(String [] d: data){
            System.out.println(d[0]+ " "+RunLengthChecker.RLEDecode(d[0]));
            Assert.assertEquals(
                RunLengthChecker.RLEDecode(d[0]),
                d[1]
            );
        }
    }
}
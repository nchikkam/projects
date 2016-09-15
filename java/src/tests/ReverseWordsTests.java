package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.ReverseWords;

public class ReverseWordsTests {

    @Test
    public static void testReverseWords(){
        String [][] data = {
            {"birds", "birds"},
            {"sample words", "words sample"},
            {"this is an example line", "line example an is this"}
        };

        for(String[] d: data){
            System.out.println(d[1]);
            System.out.println(ReverseWords.reverseWords(d[0].toCharArray()));
            Assert.assertEquals(
                    d[1].toCharArray(),
                    ReverseWords.reverseWords(d[0].toCharArray())
            );
        }
    }
}
package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.LongestRepeatedSubString;

import java.nio.file.Files;
import java.nio.file.Paths;

public class LongestRepeatedSubStringTests {

    @Test
    public void testLRS(){
        String input = "abbaabc";
        int d [] = LongestRepeatedSubString.lrs(input);
        String actual = input.substring(d[0], d[0]+d[2]);

        Assert.assertEquals(
                input.substring(d[0], d[0]+d[2]),
                "ab"
        );
    }

    @Test
    public void testLRSOnLongInput(){
        String input = "Now is the time for all good people to come to the aid of their party. Isn't \n" +
                "it now time for all good people to come to the aid of something or is it not \n" +
                "the time now to come to the aid of anything?";
        int d [] = LongestRepeatedSubString.lrs(input);
        String actual = input.substring(d[0], d[0]+d[2]);

        Assert.assertEquals(
                input.substring(d[0], d[0]+d[2]),
                " time for all good people to come to the aid of "
        );
    }

    @Test
    public void testLRSNovel() throws Exception{
        String input = new String(Files.readAllBytes(Paths.get("05medium.txt")));
        input = input.replaceAll("\t", " ");
        input = input.replaceAll("\r", "");
        input = input.replaceAll("\n", " ");
        int d [] = LongestRepeatedSubString.lrs(input);
        String actual = input.substring(d[0], d[0]+d[2]);

        Assert.assertEquals(
                actual,
                " time for all good people to come to the aid of "
        );
    }
}
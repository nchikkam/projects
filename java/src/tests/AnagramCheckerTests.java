package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.strings.AnagramGrouper;

import java.util.ArrayList;
import java.util.Hashtable;

public class AnagramCheckerTests {

    @Test
    public void testAnagramsGrouping(){
        String [] randomStrings = {
            "cars",
            "scar",
            "racs",
            "foru",
            "four",
            "creams",
            "scream"
        };

        Hashtable<String, ArrayList<String>> data =
                AnagramGrouper.groupAnagrams(randomStrings);

        /*for(String signature: data.keySet()){
            ArrayList<String> strs = data.get(signature);
            for (String s: strs){
                System.out.print(s + " ");
            }
            System.out.println();
        }*/
        Assert.assertEquals(
                3,
                data.size()
        );
    }

    @Test
    public void testAnagramsGroupingWithINTSignature(){
        String [] randomStrings = {
            "cars",
            "scar",
            "racs",
            "foru",
            "four",
            "creams",
            "scream"
        };

        Assert.assertEquals(
            3,
            AnagramGrouper.groupAnagramsWithINTSignature(randomStrings)
        );
    }
}
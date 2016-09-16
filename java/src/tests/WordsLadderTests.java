package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.WordsLadder;

import java.util.HashSet;
import java.util.Set;

public class WordsLadderTests {

    @Test
    public void testWordLadderTraversal(){
        WordsLadder subject = new WordsLadder();
        Set<String> s = new HashSet<String>();
        s.add("hot");
        s.add("dot");
        s.add("dog");
        s.add("lot");
        s.add("log");
        int steps = subject.ladderLength("hit", "cog", s);
        Assert.assertEquals(
                steps,
                5
        );
    }
}
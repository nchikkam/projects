package tests;
import org.testng.Assert;
import org.testng.annotations.Test;
import snippets.Palindrome;

public class PalindromeTests {

    @Test
    public void verifyEmptyStringIsPalindrome(){
        String empty = "";
        Palindrome subject = new Palindrome();
        Assert.assertTrue(subject.check(empty),
                "Empty String Not reported as Palindrome"
        );
    }

    @Test
    public void verifySingleCharStringIsPalindrome(){
        String single = "a";
        Palindrome subject = new Palindrome();
        Assert.assertTrue(subject.check(single),
                "Single Char String Not reported as Palindrome"
        );
    }

    @Test
    public void verifyEvenLenghtString(){
        String []evenLengthStrings = {
            "aa",
            "aabbaa",
            "abaaba",
            "12344321",
            "$%^&??&^%$"
        };
        Palindrome subject = new Palindrome();
        for(String input: evenLengthStrings) {
            Assert.assertTrue(subject.check(input),
                    "Even Length String Not reported as Palindrome"
            );
        }
    }
    @Test
    public void verifyOddLenghtString(){
        String []evenLengthStrings = {
                "1",
                "liril",
                "madam",
                "bunub",
                "$%^&?&^%$"
        };
        Palindrome subject = new Palindrome();
        for(String input: evenLengthStrings) {
            Assert.assertTrue(subject.check(input),
                    "Even Length String Not reported as Palindrome"
            );
        }
    }

    // False cases
    @Test
    public void verifyNonPalindromeString(){
        String [] nonPalindromes = {
                "12",
                "Evening",
                "great",
                "Programming",
                "WHub"
        };
        Palindrome subject = new Palindrome();
        for(String input: nonPalindromes) {
            Assert.assertFalse(subject.check(input),
                    "Even Length String Not reported as Palindrome"
            );
        }
    }

    @Test
    public void verifyLongPalindromeString(){
        String longInput = "";
        for (int i=0; i < 10000; i++)
            longInput += "1";
        Palindrome subject = new Palindrome();
        Assert.assertTrue(subject.check(longInput),
                "Even Length String Not reported as Palindrome"
        );
    }
}
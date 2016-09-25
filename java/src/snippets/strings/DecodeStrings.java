package snippets.strings;

public class DecodeStrings {

    public static int countDecoding(char []digits, int n){
        // base cases
        if (n == 0 || n == 1)
            return 1;

        int count = 0;  // Initialize count

        // If the last digit is not 0, then last digit must add to
        // the number of words
        if (digits[n-1] > '0')
            count =  countDecoding(digits, n-1);

        // If the last two digits form a number smaller than or equal to 26,
        // then consider last two digits and recur
        if (digits[n-2] < '2' || (digits[n-2] == '2' && digits[n-1] < '7') )
            count +=  countDecoding(digits, n-2);

        return count;
    }

    public static int countDecodingDP(char []digits, int n)
    {
        int count[] = new int[n+1]; // A table to store results of subproblems
        count[0] = 1;
        count[1] = 1;

        for (int i = 2; i <= n; i++)
        {
            count[i] = 0;

            // If the last digit is not 0, then last digit must add to
            // the number of words
            if (digits[i-1] > '0')
                count[i] = count[i-1];

            // If second last digit is smaller than 2 and last digit is
            // smaller than 7, then last two digits form a valid character
            if (digits[i-2] < '2' || (digits[i-2] == '2' && digits[i-1] < '7') )
                count[i] += count[i-2];
        }
        return count[n];
    }


    public static void decodeStrings(String number, String code){
        if (number == null || number.length() == 0){
            if (code != null && code.length() > 0)
                System.out.println(code);
            return;
        }

        decodeStrings(number.substring(1),
            code + (char)("a".codePointAt(0) + number.codePointAt(0) - "0".codePointAt(0) -1)
        );

        if (number.length() > 1){  // consider more cases if length is more.
            int n = Integer.parseInt(number.substring(0, 2));
            if (n <= 26){  // only if the character lies with in 26 chars.
                decodeStrings(number.substring(2), code +
                    (char)("a".codePointAt(0) + n - 1)
                );
            }
        }
    }

    public static void main(String [] args){
        decodeStrings("1123", "");
        System.out.println(countDecoding("1123".toCharArray(), 4));
        System.out.println(countDecodingDP("1123".toCharArray(), 4));

    }
}
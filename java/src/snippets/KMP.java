package snippets;

public class KMP {
    /** Failure array **/
    private static int[] failure;
    /** Constructor **/
    public static int kmp(String text, String pat)
    {
        /** pre construct failure array for a pattern **/
        failure = new int[pat.length()];
        fail(pat);
        int pos = posMatch(text, pat);
        return pos;
    }
    /** Failure function for a pattern **/
    private static void fail(String pat)
    {
        int n = pat.length();
        failure[0] = -1;
        for (int j = 1; j < n; j++)
        {
            int i = failure[j - 1];
            while ((pat.charAt(j) != pat.charAt(i + 1)) && i >= 0)
                i = failure[i];
            if (pat.charAt(j) == pat.charAt(i + 1))
                failure[j] = i + 1;
            else
                failure[j] = -1;
        }
    }
    /** Function to find match for a pattern **/
    private static int posMatch(String text, String pat)
    {
        int i = 0, j = 0;
        int lens = text.length();
        int lenp = pat.length();
        while (i < lens && j < lenp)
        {
            if (text.charAt(i) == pat.charAt(j))
            {
                i++;
                j++;
            }
            else if (j == 0)
                i++;
            else
                j = failure[j - 1] + 1;
        }
        return ((j == lenp) ? (i - lenp) : -1);
    }
}
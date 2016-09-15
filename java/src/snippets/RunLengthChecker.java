package snippets;

public class RunLengthChecker {

    public static String RLE(String start){
        StringBuffer sequence = new StringBuffer();
        for (int i = 0; i < start.length(); i++) {
            int count = 1;
            while (i + 1 < start.length() && start.charAt(i) == start.charAt(i + 1)) {
                count++;
                i++;
            }
            sequence.append(count);
            sequence.append(start.charAt(i));
        }
        return sequence.toString();
    }

    public static String RLEDecode(String start){
        // 12221131 -> 312211
        // logic repeat ith char i+1 times
        StringBuffer sequence = new StringBuffer();
        for (int i = 0; i < start.length()-1; i+=2) {  // increment twice in time bound coding, things
                                                       // like this cause troubles.
            int count = Integer.parseInt(""+start.charAt(i));
            char c = start.charAt(i+1);

            while (count > 0) {
                sequence.append(c);
                count--;
            }
        }
        return sequence.toString();
    }
}
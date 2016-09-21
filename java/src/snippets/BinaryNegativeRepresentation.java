package snippets;

import java.util.HashMap;

public class BinaryNegativeRepresentation {

    public static int getIntegerComplement(int n) {
        if (n == 0) return ~n;
        if (n == 1) return 0;

        int binaryBitsCount = Integer.SIZE - Integer.numberOfLeadingZeros(n - 1);

        int oneBitsSequence = (int)((1L << binaryBitsCount) - 1);

        //XORing the input value with the sequence of 1 bits
        return n ^ oneBitsSequence;
    }

    public static void main(String [] args){
        System.out.println(getIntegerComplement(100));
    }
}
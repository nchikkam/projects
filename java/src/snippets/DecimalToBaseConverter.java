package snippets;

public class DecimalToBaseConverter {

    public static String toHex(int decimal){
        return toBase(decimal, 16);
    }
    public static String toOctal(int decimal){
        return toBase(decimal, 8);
    }
    public static String toBase(int decimal, int base){
        char [] a = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

        int rem = 0;
        String ret = "";
        while(decimal > 0){
            rem = decimal % base;
            decimal /= base;
            ret = a[rem] + ret;
        }
        return ret;
    }

    public static void main(String [] args){
        System.out.println(toHex(255)); // FF
        System.out.println(toHex(15));  // F
        System.out.println(toHex(16));  // 10
        System.out.println(toHex(18));  // 12

        System.out.println(toOctal(255));
        System.out.println(toOctal(15));
        System.out.println(toOctal(16));
        System.out.println(toOctal(18));
    }
}
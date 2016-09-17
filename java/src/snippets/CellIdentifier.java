package snippets;

public class CellIdentifier {

    public static String toCell(int number){
        char [] a = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        };
        int base = 26;
        int rem = 0;
        String cell = "";
        while ( number >= 0 ){
            rem = number % base;
            number = (number/base)-1;
            cell = a[rem] + cell;
        }
        Boolean b;
        return cell;
    }

    public static int toNumber(String cell){
        char [] a = cell.toCharArray();
        int number = 0;
        for(char c: a) {
            number *= 26;
            number += c - 'A'+1;
        }
        return number-1;
    }


    public static void main(String [] args){
        System.out.println(toCell(255));     // IV
        System.out.println(toNumber("IV"));  // 255
        System.out.println(toNumber("AA"));  // 26
    }
}
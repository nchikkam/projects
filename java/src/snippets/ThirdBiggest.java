package snippets;

public class ThirdBiggest{

    public static int findThirdBiggest(int []arr) throws Exception{
        int first = -65537;
        int second = -65537;
        int third = -65537;

        if (arr.length < 3)
            throw new Exception("Array Lenght must be >= 3 for this algorithm");

        for(int i: arr){
            if (first < i){
                third = second;  // chain
                second = first;
                first = i;
            }else if( second < i){
                third = second;
                second = i;
            }else if (third < i){
                third = i;
            }
        }
        return third;
    }
}
package snippets;

public class MaxDifferenceBetweenIandJJcomesAfterI {

    public static void main(String [] args){
        int [] a = {2, 3, 10, 6, 4, 8, 1};// 10-2== 8
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(a)[0]);
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(a)[1]);

        int b[] = { 7, 9, 5, 6, 3, 2};
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(b)[0]);
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(b)[1]);

        int c[]= {80, 2, 6, 3, 100};
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(c)[0]);
        System.out.println(BuySellStockMaxProfit.getBuyAndSellIndices(c)[1]);
    }
}
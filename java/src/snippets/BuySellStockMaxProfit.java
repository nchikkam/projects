package snippets;

public class BuySellStockMaxProfit {

    // Question from Beating the Stock Market:
    // Find i and j that maximizes Aj – Ai, where i < j.
    public static int[] getBuyAndSellIndices(int stocks[]) {
        int min = 0;
        int maxDiff = 0;
        int buy  = 0;
        int sell = 0;
        for (int i = 0; i < stocks.length; i++) {
            if (stocks[i] < stocks[min])
                min = i;
            int diff = stocks[i] - stocks[min];
            if (diff > maxDiff) {
                buy = min;
                sell = i;
                maxDiff = diff;
            }
        }
        return new int[] {buy, sell};
    }

    public static void main(String [] args){
        int [] stocks = {5, 1, 4, 6, 7, 8, 4, 3, 7, 9};
        int [] buySell = getBuyAndSellIndices(stocks);
        System.out.println(buySell[0] + " " + buySell[1]);
    }
}
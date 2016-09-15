package snippets;

import java.util.*;

public class LongestIncreasingSubSequence {
    // below method is an inspiration from PatienceSort in Wikipedia
    public static <E extends Comparable<? super E>> int liss (E[] n){
        List<Pile<E>> piles = new ArrayList<Pile<E>>();
        // sort into piles
        for (E x : n){
            Pile<E> newPile = new Pile<E>();
            newPile.push(x);
            int i = Collections.binarySearch(piles, newPile);
            if (i < 0) i = ~i;
            if (i != piles.size())
                piles.get(i).push(x);
            else
                piles.add(newPile);
        }
        System.out.println("longest increasing subsequence has length = " + piles.size());
        return piles.size();
    }

    private static class Pile<E extends Comparable<? super E>> extends Stack<E> implements Comparable<Pile<E>>{
        public int compareTo(Pile<E> y) { return peek().compareTo(y.peek()); }
    }

    public static void main(String [] args){
        Integer[] a = {7, 2, 8, 1, 3, 4, 10, 6, 9, 5};
        System.out.println(liss(a));
    }
}
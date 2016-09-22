package snippets;

import java.util.*;

public class SortBasedOnFrequencies {

    public static <K, V extends Comparable<? super V>> Map<K, V> sortByValue(Map<K, V> map){
        Map.Entry<K,V>[] array = map.entrySet().toArray(new Map.Entry[map.size()]);

        Arrays.sort(array, new Comparator<Map.Entry<K, V>>(){
            public int compare(Map.Entry<K, V> e1, Map.Entry<K, V> e2){
                return e1.getValue().compareTo(e2.getValue());
            }
        });

        Map<K, V> result = new LinkedHashMap<K, V>(); // like ordered dict :)
        for (Map.Entry<K, V> entry : array)
            result.put(entry.getKey(), entry.getValue());

        return result;
    }

    public static Map<Integer, Integer> sortBasedOnFrequencies(int [] a){
        Hashtable<Integer, Integer> map = new Hashtable<Integer, Integer>();
        for( int v: a){
            if(map.containsKey(v))
                map.put(v, map.get(v)+1);
            else
                map.put(v, 1);
        }
        return sortByValue(map);
    }

    public static void main(String [] args){
        int a[] = {2,2,2,1,1,1,3,4,8,2};

        Map<Integer, Integer> result = sortBasedOnFrequencies(a);
        for( Integer v: result.keySet())
            System.out.print(v + " ");
        System.out.println();
    }
}
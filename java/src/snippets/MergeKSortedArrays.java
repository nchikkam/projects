package snippets;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class MergeKSortedArrays {
    /*
        Idea:
          Any scenario where there is a need to  pickup samples  or  sorted data
          set, use a heap of capacity[no of channels].   Read  the  channel data
          update heap, pick the element that comes in the order, insert new data
          into heap, advance that particular channel or stream.

          Design Decisions:
          Heap has been kept generic, however a new envelop has been created  to
          combine the index that gives the stream to read from and the value  to
          be presented.

          Complexity:
          O( N * log S ): Where N is the Maximum length of the Streams,  S  is no
                          of Streams.
     */

    static class Entry{    // ToDo: UGLY to have this Composition. Enhance Heap to
        public int index;  // ToDo:             have index along with key Storage.
        public Integer number;
        public Entry(int index, Integer input){
            this.index = index;
            this.number = input;
        }
    }
    static class MyComparator implements Comparator<Entry> { // creating class instead of anonymous one
        public int compare(Entry one, Entry two) {
            if (one.number > two.number) {
                return 1;
            } else if (one.number < two.number) {
                return -1;
            } else {
                return 0;
            }
        }
    }
    public static void merge(List<LinkedList<Integer>> inputs){
        int n = inputs.size();
        HeapSort.MinHeap caster = new HeapSort.MinHeap(n, new MyComparator());
        for (int i = 0; i < n; i++) {
            Entry element = new Entry(i, inputs.get(i).remove());
            if (element != null)
                caster.insert(element);
        }

        while (!caster.isEmpty()){
            Entry element = (Entry) caster.remove();  // min Entry
            System.out.println(element.number); //data

            if( inputs.get(element.index).size() > 0){  // that channel is not done yet.
                Integer data = inputs.get(element.index).remove();
                element = new Entry(element.index, data);
                caster.insert(element);
            }
        }
    }

    public static void main(String [] args){
        int a[] = {1, 3, 5, 7, 9, 10, 34, 58};
        int b[] = {2, 11, 23, 24, 32, 48, 98, 158};
        int c[] = {4, 6, 8, 12, 14, 17, 28, 558};

        List<LinkedList<Integer>> channels = new ArrayList<LinkedList<Integer>>();
        channels.add(new LinkedList<Integer>());
        channels.add(new LinkedList<Integer>());
        channels.add(new LinkedList<Integer>());

        for(int v: a) channels.get(0).add(v);
        for(int v: b) channels.get(1).add(v);
        for(int v: c) channels.get(2).add(v);

        merge(channels);
    }
}
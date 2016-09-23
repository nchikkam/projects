package snippets;

import java.util.Comparator;

public class HeapSort {

    public static class MinHeap<E> {
        Comparator<E> comparator;
        private E [] heapArray;   // storage to store items in heap
        public  int size;	// running size of the heap
        public  int maxsize;	// in other words, capacity

        private static final int MIN_INDEX = 1;

        public MinHeap(int maxsize, Comparator<E> compare){
            this.comparator = compare;
            this.maxsize = maxsize;
            this.size = 0;
            heapArray = (E[]) new Object[this.maxsize + 1];
            heapArray[0] = null;  // heap definition, we never use index '0'
        }

        // childs of a node will present at 2*parent's index for left and +1 for right
        private int parent(int pos){
            return pos / 2;
        }

        private int leftChild(int pos){
            return (2 * pos);
        }

        private int rightChild(int pos){
            return (2 * pos) + 1;
        }

        // this swaps the nodes and updates the pointers inside.
        private void swap(int a, int b){
            E temp = heapArray[a];
            heapArray[a] = heapArray[b];
            heapArray[b] = temp;
        }

        public void minHeapify(int pos){
            int left = leftChild(pos);
            int right = rightChild(pos);
            int small;

            if (left <= size &&  comparator.compare(heapArray[left], heapArray[pos]) < 0)
                small= left;
            else
                small = pos;

            if (right <= size && comparator.compare(heapArray[right], heapArray[pos]) < 0)
                small= right;

            if (small != pos) {
                swap( pos, small);
                minHeapify( small );
            }
        }

        public void insert(E element){
            if (size < maxsize) {
                heapArray[++size] = element;
                int current = size;
                while (current >= 2 && comparator.compare(heapArray[current], heapArray[parent(current)])< 0 ) {
                    swap(current, parent(current));
                    current = parent(current);
                }
            }
            minHeap();
        }

        public void print(){
            for (int i = 1; i <= size; i++ ){
                System.out.println(heapArray[i] + "(" + heapArray[i] + ")");
            }
        }

        public void minHeap(){
            for (int pos = (size / 2); pos >= 1 ; pos--)
                minHeapify(pos);
        }

        public E remove(){
            E min = heapArray[MIN_INDEX];
            heapArray[MIN_INDEX] = heapArray[size--];
            minHeapify(MIN_INDEX);
            minHeap();
            return min;
        }

        public E get(int pos){
            return heapArray[pos];
        }
        public boolean isEmpty(){ return size==0; };
    }

    public static void main(String [] args){
        Integer a[] = {4, 3, 6, 2, 5, 7, 1, 9, 8};

        class MyComparator implements Comparator<Integer> {
            public int compare(Integer one, Integer two) {
                if (one > two) {
                    return 1;
                } else if (one < two) {
                    return -1;
                } else {
                    return 0;
                }
            }
        }

        MinHeap heap = new MinHeap(a.length, new MyComparator());
        for(int v: a)
            heap.insert(v);
        int i =0;
        Integer []b = new Integer[a.length];
        while(i < a.length){
            b[i] = (Integer) heap.remove();
            i++;
        }

        for(int v: b)
            System.out.println(v);
        System.out.println();
    }
}
package snippets;

public class MinHeap {
    private int [] heapArray;
    public  int size;
    public  int maxsize;

    private static final int MIN_INDEX = 1;

    public MinHeap(int maxsize)
    {
        this.maxsize = maxsize;
        this.size = 0;
        heapArray = new int[this.maxsize + 1];
        heapArray[0] = -65535;  // heap definition, we never use index '0'
    }

    private int parent(int pos){
        return pos / 2;
    }

    private int leftChild(int pos){
        return (2 * pos);
    }

    private int rightChild(int pos){
        return (2 * pos) + 1;
    }

    private void swap(int a, int b){
        int temp = heapArray[a];
        heapArray[a] = heapArray[b];
        heapArray[b] = temp;
    }

    public void minHeapify(int pos){
        int left = leftChild(pos);
        int right = rightChild(pos);
        int small;

        if (left <= size &&  heapArray[left] < heapArray[pos])
            small= left;
        else
            small = pos;

        if (right <= size && heapArray[right] < heapArray[pos])
            small= right;

        if (small != pos) {
            swap( pos, small);
            minHeapify( small );
        }
    }

    public void insert(int element){
        if (size < maxsize) {
            heapArray[++size] = element;
            int current = size;

            while (current >= 2 && heapArray[current] < heapArray[parent(current)]) {
                swap(current, parent(current));
                current = parent(current);
            }
        }
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

    public int remove(){
        int min = heapArray[MIN_INDEX];
        heapArray[MIN_INDEX] = heapArray[size--];
        minHeapify(MIN_INDEX);
        return min;
    }
}
class MinHeap {
	private HeapNode [] heapArray;
	public  int size;
	public  int maxsize;

	private static final int MIN_INDEX = 1;

	public MinHeap(int maxsize)
	{
		this.maxsize = maxsize;
		this.size = 0;
		heapArray = new HeapNode[this.maxsize + 1];
		heapArray[0] = null;  // heap definition, we never use index '0'
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
		Object temp = heapArray[a];
		heapArray[a] = heapArray[b];
		heapArray[b] = temp;
	}

	public void minHeapify(int pos){
		int left = leftChild(pos);
		int right = rightChild(pos);
		int small;

		if (left <= size &&  heapArray[left].count < heapArray[pos].count)
			small= left;
		else
			small = pos;

		if (right <= size && heapArray[right].count < heapArray[pos].count)
			small= right;

		if (small != pos) {
			swap( pos, small);
			minHeapify( small );
		}
	}

	public void insert(HeapNode element){
		if (size < maxsize) {
			heapArray[++size] = element;
			int current = size;
			element.trieNode.pointerToHeap = size;

			while (current >= 2 && heapArray[current].count < heapArray[parent(current)].count) {
				swap(current, parent(current));
				current = parent(current);
			}
		}
	}

	public void print(){
		for (int i = 1; i <= size; i++ ){
			System.out.println(heapArray[i] + "(" + heapArray[i].count + ")");

		}
	}

	public void minHeap(){
		for (int pos = (size / 2); pos >= 1 ; pos--)
			minHeapify(pos);
	}

	public HeapNode remove(){
		HeapNode min = heapArray[MIN_INDEX];
		heapArray[MIN_INDEX] = heapArray[size--];
		minHeapify(MIN_INDEX);
		return min;
	}

	public HeapNode get(int pos){
		return heapArray[pos];
	}
	public HeapNode[] getAllPhrases(){return heapArray;}
}
import java.util.ArrayList;
import java.util.HashMap;

/*
	The Approach:
		A straight forward solution for this would be to use a Hashmap
		that maintains count of each phrase. As and when the phrases are
		read from the input stream, the map is updated. Once the stream
		is finished, the map could be sorted based on the value counts and
		returning the top-x phrases.

		The advantage of above appraoch is that it is fast. A drawback is
		that it needs lot of space.

	Optimal and A Good Approach:
	 	A comibination of Datastructures Namely 'Trie' and MinHeap would
	 	be good to strategically solve this problem. Below solution uses
	 	 these constructs.

	 	Idea:
	 		Store the phrases in the Trie [generally an Array is used as
	 		lookup table at each node. In the below, a Hashmap is used instead
	 		to save space and store just what it needed]

	 		A Trie Node contains:
	 			branches: a hashmap<string, trie>
	 			pointerTOItsIndex if it is in the top 'x' limit. If its not, then
	 				this value will hold -1.
	 			a flag to denote that its the end of the phrase.

			 MinHeap:
			 	For simple reasons and simplicity this Heap was modled to have
			 	just the HeapNode type [Trie, count and phrase]

			 TopPhrases:
			 	The main class that uses both above and acts as driver to process
			 	input and keep the heap updates.

		The total time complexity of the whole process is O(Nlogn) where N is the input
		size [total no of phrases]
		explanation:
			Reading each phrase, traversing the trie from top to bottom by character
			lookup, if the phrase is frequent, updating the heap.
			O(N) * O(logn)
				==> O(N) for reading whole input
				==> logn each time for updating the heap.
 */

public class TopPhrases{

	Trie root;   		// root node of entire trie
	MinHeap kHeap;		// heap to keep top x nodes.

	public TopPhrases(int topKLimit){	//sets the heap limit to top-X
		root = new Trie();
		kHeap = new MinHeap(topKLimit);
	}

	public void process(String input){
		root.insert(input, kHeap);
	}

	public HeapNode[] getTopKPhrases(){
		return kHeap.getAllPhrases();
	}


	public static void main(String [] args){
		String [] lines = {
			"1|1|1|1|1",
			"2|2|2|2|2",
			"3|3|4|4|4",
			"5|5|6|6|6"
		};

		TopPhrases obj = new TopPhrases(3);

		for (String line: lines){
			String []phrases = line.split("\\|");
			for(String phrase: phrases) {
				phrase = phrase.trim();
				obj.root.insert(phrase, obj.kHeap);
			}
		}
		System.out.println("-------Top X Phrases And their Frequencies:---------");
		obj.kHeap.print();
	}

	// Inner classes
	class Trie{
		// Since the phrases contain special characters, numbers and space, a hashmap
		// has been chosen instead of array as it keeps the design clean.
		HashMap<Character, Trie> branches;
		boolean isLast;
		int  	count; // keeps the times a phrase ended at this node in count.
		int    	pointerToHeap;   // this makes the datastructure more transperant as updating
								 // the count with in the trie, auto updates the heap's trie
		public Trie(){
			pointerToHeap = -1;  // A hack also to describe that its not in the heap yet.
			isLast = false;
			branches = new HashMap<Character, Trie>();
			count = 0;			// count of phrase end until this node from top.
		}

		/*
			This method updates Heap each time a phrase is traversed using Trie.
			When a phrase reaches the trie last node, its count is incremented
			and this method is called. If pointer to heap is -1, it means this node
			is new to heap, it goes basically by 3 conditions.
		 */
		public void updateMinHeap(Trie node, MinHeap heap, String phrase){
			if (node.pointerToHeap != -1) {  // word is in top x heap, update count and heapify to have min at top
				HeapNode found = heap.get(node.pointerToHeap);
				found.count = node.count;  // update the count of the node found in heap to reflect trie's status
				heap.minHeapify(node.pointerToHeap);
			}else if (heap.size < heap.maxsize ){
				HeapNode newNode = new HeapNode();
				newNode.count = node.count;
				newNode.phrase = phrase;
				newNode.trieNode = node; // keep node in MinHeap
				heap.insert(newNode);
				heap.minHeap();
			}else if (node.count > heap.get(1).count) {     // heap is full, decide to keep min of minHeap or current node based on count
				HeapNode minNode = heap.get(1);
				minNode.trieNode.pointerToHeap = -1; //notify that it will not exist in heap anymore as we delete it
				minNode.count = node.count;
				minNode.phrase = phrase;
				minNode.trieNode = node;
				node.pointerToHeap = 1;
				heap.minHeapify(1);
			}
		}

		public void insert(String phrase, MinHeap heap) {  // O(N) where N is the lenght of the longest phrase
			Trie node = this;
			phrase = phrase.toLowerCase();
			for(int i=0; i<phrase.length(); i++){
				char c = phrase.charAt(i);
				if(node.branches.containsKey(c))
					node=node.branches.get(c);
				else{
					Trie temp = new Trie();
					node.branches.put(c, temp);
					node = temp;
				}
			}
			node.isLast = true; // mark this node as leaf
			node.count += 1;    // either we just added a new entry or tried to duplicate

			// update min heap
			updateMinHeap(node, heap, phrase);
		}

		// useful debugging method to see the trie contents.
		public void print(ArrayList<Character> phrase){ // O(N*M) Where N is the length of the longest phrase
			// and M is no of phrases in the whole input set
			Trie root= this;
			if (root.isLast) {
				for (Character c: phrase){
					System.out.print(c);
				}
				System.out.print(":"+root.count);
				System.out.println();
			}
			for(Character c : root.branches.keySet()){
				phrase.add(new Character(c));
				root.branches.get(c).print(phrase);
				phrase.remove(phrase.size()-1);
			}
		}
	}

	// Below is the type that is actaully stored in the heap.
	class HeapNode{
		Trie trieNode;  // a pointer to the trienode - to access it faster and update when node is removed from heap
		int		count;	// no of times this phrase occured
		String 	phrase; // actual phrase

		public String toString(){
			return phrase;
		}
	}

	// Standard minHeap utility which maintains the condition that 'every parent node
	// contains a value less than its childs'
	class MinHeap {
		private HeapNode [] heapArray;   // storage to store items in heap
		public  int size;	// running size of the heap
		public  int maxsize;	// in other words, capacity

		private static final int MIN_INDEX = 1;

		public MinHeap(int maxsize)
		{
			this.maxsize = maxsize;
			this.size = 0;
			heapArray = new HeapNode[this.maxsize + 1];
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
			HeapNode temp = heapArray[a];
			heapArray[a] = heapArray[b];
			heapArray[b] = temp;

			// Also update the pointersToMinHeap of both nodes so that trie has latest updated
			// state of heap
			int t = heapArray[a].trieNode.pointerToHeap;
			heapArray[a].trieNode.pointerToHeap = heapArray[b].trieNode.pointerToHeap;
			heapArray[b].trieNode.pointerToHeap = t;
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
}
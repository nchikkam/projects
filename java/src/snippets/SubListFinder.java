package snippets;

public class SubListFinder {
    public class LinkedList{
        public String data;
        public LinkedList next;
    }

    public static int findSubList(LinkedList list, LinkedList sublist){
        int pos = 0;
        if(sublist!=null) {           // O(N*M)
            while (list != null) {    // O(N) - N is length of list
                LinkedList main = list;
                LinkedList sub = sublist;

                while (sub != null) {   // O(M)  - M is length of sublist
                    if (main.data != sub.data)
                        break;
                    main = main.next;
                    sub = sub.next;
                }
                if (sub == null)
                    return pos;
                ++pos;
                list = list.next;
            }
        }
        return -1;
    }
}
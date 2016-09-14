package snippets;

public class SubListFinder {
    public class LinkedList{
        public String data;
        public LinkedList next;
    }

    public static int findSubList(LinkedList list, LinkedList sublist){
        int pos = 0;
        if(sublist!=null) {
            while (list != null) {
                LinkedList main = list;
                LinkedList sub = sublist;

                while (sub != null) {
                    System.out.println("Comparing: " + main.data + " " + sub.data);
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
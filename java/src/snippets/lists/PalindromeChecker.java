package snippets.lists;

import java.util.Stack;

public class PalindromeChecker {
    public static class Node{
        public char data;
        public Node next;

        public Node(char data){
            this.data = data;
        }

        public Node create(char data){
            return new Node(data);
        }
    }

    public static boolean isPalindromeReverseFullList(Node head) {
        if(head == null)
            return true;

        Node p = head;
        Node prev = new Node(head.data);

        while(p.next != null){
            Node temp = new Node(p.next.data);
            temp.next = prev;
            prev = temp;
            p = p.next;
        }

        Node p1 = head;
        Node p2 = prev;

        while(p1!=null){
            if(p1.data != p2.data)
                return false;

            p1 = p1.next;
            p2 = p2.next;
        }

        return true;
    }

    public static boolean isPalindromeSecondHalfReverseList(Node head) {  // good one
        if(head == null || head.next==null) return true;
        Node fast = head;
        Node slow = head;

        while(fast.next!=null && fast.next.next!=null){ // find mid node
            fast = fast.next.next;
            slow = slow.next;
        }

        Node secondHead = slow.next;
        slow.next = null; // cut the half list for termination

        Node p1 = secondHead;
        Node p2 = p1.next;

        while(p1!=null && p2!=null){
            Node temp = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = temp;
        }

        secondHead.next = null;  // second part end

        Node p = (p2==null?p1:p2);  // case to handle mid part
        Node q = head;
        while(p!=null){
            if(p.data != q.data)
                return false;
            p = p.next;
            q = q.next;
        }
        return true;
    }

    public static boolean isPalindromeReverseFirstHalf(Node head) {  // good one
        if(head == null || head.next==null) return true;
        Node fast = head;
        Node slow = head;
        Node next = null;

        Node rev = null;
        while(fast.next!=null && fast.next.next!=null){
            fast = fast.next.next;
            next = slow.next;
            // keep reversing the first half while finding mid.
            slow.next = rev;
            rev = slow;

            slow = next;
        }
        slow.next=rev;
        rev = slow;

        Node p;
        if (fast.next!=null)
            p = rev;
        else
            p = fast.next;

        Node q = slow; // second half.

        while(p!=null){
            if(p.data != q.data)
                return false;
            p = p.next;
            q = q.next;
        }
        return true;
    }

    public static boolean isPalindromeUsingStack(Node head) {
        if(head == null || head.next==null) return true;
        Node fast = head;
        Node slow = head;

        Stack<Node> rev = new Stack<Node>();
        while(fast.next!=null && fast.next.next!=null){
            fast = fast.next.next;
            rev.push(slow);
            slow = slow.next;
        }

        if(fast.next!=null)
            rev.push(slow);  //only two nodes

        Node q = slow.next; // second half.
        while(q!=null && !rev.empty()){
            Node p = rev.pop();
            if(p.data != q.data)
                return false;
            q = q.next;
        }
        return rev.empty() && q == null;
    }

    public static Node getHead(){
        char [] data = "aba".toCharArray();
        Node head = new Node('a');
        Node temp = head;
        for(int i=1;i< data.length; i++) {
            temp.next = new Node(data[i]);
            temp = temp.next;
        }
        return head;
    }
    public static void main(String [] args){

        System.out.println(isPalindromeReverseFullList(getHead()));
        System.out.println(isPalindromeSecondHalfReverseList(getHead()));

        System.out.println(isPalindromeReverseFirstHalf(getHead()));
        System.out.println(isPalindromeUsingStack(getHead()));
    }
}
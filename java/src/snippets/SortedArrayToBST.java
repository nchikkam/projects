package snippets;

public class SortedArrayToBST {

    public static class Node {
        public int data;
        public Node left, right;
        public Node(int data){
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public static Node toBST(int []a, int start, int end){
        if (start > end) return null;
        int mid = start + (end-start)/2;
        Node root   = new Node(a[mid]);
        root.left   = toBST(a, start, mid-1);
        root.right  = toBST(a, mid+1, end);
        return root;
    }

    public static void inorder(Node root){
        if(root != null){
            inorder(root.left);
            System.out.print(root.data + " ");
            inorder(root.right);
        }
    }

    public static void main(String [] args){
        int a[] = {1, 2, 3, 4, 5, 6, 7};
        Node root = toBST(a, 0, a.length-1);
        inorder(root);

        System.out.println();
        int b[] = {1, 2, 3};
        root = toBST(b, 0, b.length-1);
        inorder(root);

        System.out.println();
        int c[] = {1, 2};
        root = toBST(c, 0, c.length-1);
        inorder(root);
    }
}
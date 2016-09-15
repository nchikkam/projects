package snippets;

public class StackWithMin {

    Entry stack[];
    int   top;

    class Entry{
        public int data;
        public int min;
        public Entry(int data, int min){
            this.data = data;
            this.min = min;
        }
    }

    public StackWithMin(){
        stack = new Entry[100]; // some size
        top = 0;
    }
    public Entry peek() throws Exception{
        if (top ==0 )
            throw new Exception("Stack is Empty");
        return stack[top-1];
    }

    public int min(int a, int b){
        if(a > b) return b;
        return a;
    }

    public void push(int data) throws Exception{
        int min = data;
        if (top > 0){
            Entry last = peek();
            min = last.min;
        }
        Entry entry = new Entry(data, min(data, min));
        stack[top++] = entry;
    }

    public int getMin() throws Exception{
        return peek().min;
    }

    public int pop() throws Exception{
        if (top == 0)
            throw new Exception("Stack Empty");

        Entry t = stack[--top];
        return t.data;
    }

    public static void main(String [] args) throws Exception{
        StackWithMin stack = new StackWithMin();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        stack.push(-1);
        stack.push(9);
        stack.push(7);
        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

        System.out.println(stack.getMin());
        System.out.println(stack.pop());

    }
}
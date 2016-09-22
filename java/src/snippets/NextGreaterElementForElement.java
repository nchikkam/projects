package snippets;

import java.util.Stack;

public class NextGreaterElementForElement {

    public static void nextGreaterElement_O_N_2(int [] a){
        for(int i=0; i< a.length; i++){
            int j = i+1;
            while(j< a.length && a[i]>a[j])  // find next greater
                j++;
            if(j < a.length)
                System.out.println(a[i]+ " "+a[j]);
            else
                System.out.println(a[i]+ " "+-1);
        }
    }

    /*
        Below code is O(N) with constant operations to use
        stack. The worst case happens when the elements are
        in decreasing order.
        1) Push the first element to stack.
        2) Pick rest of the elements one by one and follow following steps in loop.
           a) Mark the current element as next.
           b) If stack is not empty, then pop an element from stack and compare it with next.
           c) If next is greater than the popped element, then next is the next greater element
              for the popped element.
           d) Keep popping from the stack while the popped element is smaller than next. next
              becomes the next greater element for all such popped elements
           g) If next is smaller than the popped element, then push the popped element back.
        3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next
           element for them.
     */
    public static void nextGreaterElement(int a[]){
        int i = 0;
        Stack<Integer> stack = new Stack<Integer>();
        int element, next;

        for (i=0; i<a.length; i++){
            /* push the first element to stack */
            if(i == 0){
                stack.push(a[0]);
                continue;
            }

            next = a[i];

            if (! stack.empty()){
                element = stack.pop();
                while (element < next){
                    System.out.println(element + " -> "+ next);
                    if(stack.empty()) break;
                    element = stack.pop();
                }

                /* If element is greater than next,
                then push the element back */
                if (element > next)
                    stack.push(element);
            }

            /* push next to stack so that we can
            find next greater for it */
            stack.push(next);
        }

        while (!stack.empty()){
            element = stack.pop();
            next = -1;
            System.out.println(element + " -> "+ next);
        }
    }

    public static void main(String [] args){
        int a[] = {4, 15, 2, 9, 20, 11, 13};
        nextGreaterElement_O_N_2(a);
        nextGreaterElement(a);
    }
}
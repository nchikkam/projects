package snippets;

import java.io.IOException;
import java.util.HashMap;
import java.util.Stack;

public class PostfixExpressionEvaluator {

    public static boolean isOperator(String op){
        HashMap<String, String> operators =
            new HashMap<String, String>(){
                {
                    put("+", "");
                    put("-", "");
                    put("*", "");
                    put("/", "");
                }
        };
        if (operators.containsKey(op))
            return true;
        return false;
    }

    public static int calc(String op, int left, int right){
        int ret = 0;
        if (op == "+")
            ret = left + right;
        if (op == "-")
            ret =left - right;
        if (op == "*")
            ret =left * right;
        if (op == "/")
            ret =left / right;
        return ret;
    }

    public static String eval(String[] tokens){
        Stack<String> stack = new Stack<String>();

        for(String t: tokens){
            if (isOperator(t)){
                int right = Integer.parseInt(stack.pop());
                int left  = Integer.parseInt(stack.pop());
                stack.push(new Integer(calc(t, left, right)).toString());
            }else
                stack.push(t);
        }
        return stack.pop();
    }

    public static void main(String[] args) throws IOException {
        String[] tokens = new String[] { "2", "1", "+", "3", "*" };
        System.out.println(eval(tokens));
    }
}
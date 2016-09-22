package snippets;

import java.util.HashMap;
import java.util.Map;

public class LargestSubArrayWithEqual01s {

    public static int [] largestSubArrayWithEqualBits_O_N_3(int [] a){
        int maxLength = Integer.MIN_VALUE;
        int start = -1;
        int end =  -1;
        for(int i =0; i < a.length; i++){
            for(int j=i+1; j < a.length; j++){
                int localMax = Integer.MIN_VALUE;
                int zeros = 0;
                int ones = 0;
                for(int k = i; k <= j; k++){
                    if (a[k] == 0)
                        zeros++;
                    else
                        ones++;
                }
                if (zeros == ones){
                    if(localMax < zeros+ones)
                        localMax = zeros+ones;
                    if( maxLength < localMax){
                        maxLength = localMax;
                        start = i;
                        end = j;
                    }
                }
            }
        }
        return new int[]{
            maxLength==Integer.MIN_VALUE?-1:maxLength,
            start,
            end
        };
    }

    public static int [] largestSubArrayWithEqualBits_O_N_2(int [] a){
        int sum = 0;
        int maxsize = -1, startindex = 0;
        int endindex = 0;
        int n = a.length;

        for (int i = 0; i < n - 1; i++){
            sum = (a[i] == 0) ? -1 : 1;
            for (int j = i + 1; j < n; j++){
                if(a[j] == 0) sum += -1;
                else sum += 1;
                if (sum == 0 && maxsize < j - i + 1){
                    maxsize = j - i + 1;
                    startindex = i;
                }
            }
        }
        endindex = startindex+maxsize-1;
        if (maxsize == -1) {
            return new int[]{-1, -1, -1};
        }
        return new int [] {maxsize, startindex, endindex};
    }

    public static int [] largestSubArrayWithEqualBits(int a[]){
        /*
            If there was a sum which is 0, record it, compare it next time
            we encounter the same sum.
         */
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        int sum = 0;
        int max_len  = -1;
        int s = -1;
        int e = -1;
        for(int i = 0; i < a.length;i++){
            if(a[i]==0) a[i] = -1;  // mask 0 to -1

            sum+=a[i];

            if(sum == 0){   // kadanes logic - max subarray sum from integer array
                s = 0;
                e = i;
                max_len = i + 1;
            }

            if(m.containsKey(sum)){       // find the max len, start and end indices
                int prev = m.get(sum);
                int ans = i- prev;
                if(ans > max_len){
                    max_len = ans;
                    s = prev+1;
                    e = i;
                }
            }else{
                m.put(sum, i);  // store sum up to that index and index in map
            }

            if(a[i] == -1) a[i] = 0;// unmask
        }
        return new int [] {max_len, s, e};
    }

    public static void main(String [] args){
        int []a = {1, 0, 1, 1, 1, 0, 0, 0, 1};
        int [] data =largestSubArrayWithEqualBits_O_N_3(a);
        System.out.println(data[0]);
        System.out.println(data[1]);
        System.out.println(data[2]);
        int d1[]= largestSubArrayWithEqualBits_O_N_2(a);
        System.out.println(d1[0]);
        System.out.println(d1[1]);
        System.out.println(d1[2]);
        int d11[]= largestSubArrayWithEqualBits(a);
        System.out.println(d11[0]);
        System.out.println(d11[1]);
        System.out.println(d11[2]);

        int [] b = {1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1};
        int [] d =largestSubArrayWithEqualBits_O_N_3(b);
        System.out.println(d[0]);
        System.out.println(d[1]);
        System.out.println(d[2]);
        int d2[]= largestSubArrayWithEqualBits_O_N_2(b);
        System.out.println(d2[0]);
        System.out.println(d2[1]);
        System.out.println(d2[2]);
        int dd[]= largestSubArrayWithEqualBits(b);
        System.out.println(dd[0]);
        System.out.println(dd[1]);
        System.out.println(dd[2]);

        int c[] = {1, 1, 1, 1, 1, 1 ,1, 0 ,0, 0 ,0, 1, 1 ,1 ,1, 1 ,1};
        int [] cd =largestSubArrayWithEqualBits_O_N_3(c);
        System.out.println(cd[0]);
        System.out.println(cd[1]);
        System.out.println(cd[2]);
        int cd2[]= largestSubArrayWithEqualBits_O_N_2(c);
        System.out.println(cd2[0]);
        System.out.println(cd2[1]);
        System.out.println(cd2[2]);
        int cdd[]= largestSubArrayWithEqualBits(c);
        System.out.println(cdd[0]);
        System.out.println(cdd[1]);
        System.out.println(cdd[2]);
    }
}
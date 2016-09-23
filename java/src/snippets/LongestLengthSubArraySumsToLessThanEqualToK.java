package snippets;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class LongestLengthSubArraySumsToLessThanEqualToK {

    public static int maxSubArrayLen(int[] nums, int k) {
        int sum = 0, max = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            sum = sum + nums[i];
            if (sum == k) max = i + 1;
            else if (map.containsKey(sum - k)) max = Math.max(max, i - map.get(sum - k));
            if (!map.containsKey(sum)) map.put(sum, i);
        }
        return max;
    }

    public static int findLongestSubarrayLessEqualK(List<Integer> A, int k) {
        // Build the prefix sum according to A.
        List<Integer> prefixSum = new ArrayList<>();
        int sum = 0;
        for (int a : A) {
            sum += a;
            prefixSum.add(sum);
        }

        // Early returns if the sum of A is smaller than or equal to k.
        if (prefixSum.get(prefixSum.size() - 1) <= k) {
            return A.size();
        }

        // Builds minPrefixSum.
        List<Integer> minPrefixSum = new ArrayList<>(prefixSum);
        for (int i = minPrefixSum.size() - 2; i >= 0; --i) {
            minPrefixSum.set(i,
                    Math.min(minPrefixSum.get(i), minPrefixSum.get(i + 1)));
        }

        int a = 0, b = 0, maxLength = 0;
        while (a < A.size() && b < A.size()) {
            int minCurrSum = a > 0 ? minPrefixSum.get(b) - prefixSum.get(a - 1)
                    : minPrefixSum.get(b);
            if (minCurrSum <= k) {
                int currLength = b - a + 1;
                if (currLength > maxLength) {
                    maxLength = currLength;
                }
                ++b;
            } else { // minCurrSum > k.
                ++a;
            }
        }
        return maxLength;
    }

    public static void main(String[] args){
        int a[] = {1, 2, 3};
        List<Integer> l = new ArrayList<Integer>();
        for (int d: a)
            l.add(d);
        System.out.println(findLongestSubarrayLessEqualK(l, 3));
        System.out.println(maxSubArrayLen(a, 3));

        int b [] = {1, 1, 1, 2, 1, 1, 1, 4, 4, 1, 2 ,3, 4, 1};
        l = new ArrayList<Integer>();
        for (int d: b)
            l.add(d);
        System.out.println(findLongestSubarrayLessEqualK(l, 7));
        System.out.println(maxSubArrayLen(b, 7));

        int c[] = {1,1,1,1,3,7};
        l = new ArrayList<Integer>();
        for (int d: c)
            l.add(d);
        System.out.println(findLongestSubarrayLessEqualK(l, 7));
        System.out.println(maxSubArrayLen(c, 7));

        int d[] = {1, 2, 3, 4};
        l = new ArrayList<Integer>();
        for (int f: d)
            l.add(f);
        System.out.println(findLongestSubarrayLessEqualK(l, 4));
        System.out.println(maxSubArrayLen(d, 4));
    }
}
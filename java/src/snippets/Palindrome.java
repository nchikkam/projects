package snippets;

public class Palindrome{

	/*
		The time complexity of this algorithm is O(N).
		It maintains two poiners to check the indices
		and advances the one to go to right side position
		and reduces the other one to move to the left.

		At any time if it finds a mismatch, it returns
		false so as not to continue.
	 */
	public boolean check(String input){
		int left = 0;
		int right = input.length()-1;
		while (left < right){
			if (input.charAt(left) != input.charAt(right) )
				return false;
			left += 1;
			right -= 1;
		}
		return true;
	}

	public static void main(String [] args){

		String [] inputs = {
			"1221",
			"a",
			"ababa",
			"11",
			"-a-",
			"",
			"12321",
			"ab",
			"ba",
			"123456789101987654321",
			"12345678911987654321"
		};
		Palindrome obj = new Palindrome();

		for(String input: inputs){
			System.out.println(input +" palindrome ? " + obj.check(input));
		}
	}
}
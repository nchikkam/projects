package snippets;

public class FindMinDistanceBetweenXandY {


    public static int findMinDistance(int []a, int x, int y) {
        int index=-1, res=0;

        for(int i=0; i <= a.length-1; i++){
            if(a[i]==x||a[i]==y){
                index=i;
                break;
            }
        }
        int distance = Integer.MAX_VALUE;

        for(int i=index; i<= a.length-1; i++){
            if( a[i] == x || a[i] == y ){
                if(a[i] != a[index])
                    distance = Math.min(distance, i - index);
                else
                    index=i;
            }
        }
        return distance;
    }

    public static void main(String [] args){
        int []a = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3, 6};
        System.out.println(findMinDistance(a, 3, 6)); //1

        int []b = {2, 5, 3, 5, 4, 4, 2, 3};
        System.out.println(findMinDistance(b, 3, 2)); //1

        int []c = {3, 4, 5};
        System.out.println(findMinDistance(c, 3, 5)); //2

        int []d = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3};
        System.out.println(findMinDistance(d, 3, 6)); //4
    }
}
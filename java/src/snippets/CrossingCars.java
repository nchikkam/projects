package snippets;

public class CrossingCars {

    public static int countCrossingCars_bruteforce(int[] cars){
        /*
            Find first east going car or intersection, count other
            cars from there.
            if reached last east going car, process done.
            else, find next east going car, repeate the process
            O(N^2)
         */
        int crossings = 0;
        int i =0;
        while(i < cars.length){
            // find first east going
            while(i < cars.length && cars[i] != 0)  // find west going car
                i++;

            if( i >= cars.length) break;  // if last car, return

            int j = i+1;
            while(j < cars.length){   // find crossing cars
                if (cars[j] == 1)
                    crossings++;
                j++;
            }
            i++;
        }
        return crossings;
    }

    public static int countCrossingCars(int[] cars){
        int crossings = 0;
        int eastGoing = 0;
        for(int car: cars){
            if (car == 0)
                eastGoing += 1;
            else{
                crossings += eastGoing;
            }
        }
        return crossings;
    }

    public static void main(String [] args){
        int [] cars = {0, 1, 0, 1, 1};
        System.out.println(countCrossingCars_bruteforce(cars));  //5
        System.out.println(countCrossingCars(cars));  //5

        int [] a= {0, 1, 0, 0, 1};
        System.out.println(countCrossingCars_bruteforce(a)); //4
        System.out.println(countCrossingCars(a)); //4

        int [] b= {1, 0, 1, 1, 0};
        System.out.println(countCrossingCars_bruteforce(b)); //2
        System.out.println(countCrossingCars(b)); //2

        int [] c= {1, 1, 1, 0, 1};
        System.out.println(countCrossingCars_bruteforce(c)); //1
        System.out.println(countCrossingCars(c)); //1

    }
}
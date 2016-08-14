open Printf;;
open List;;

let sum = List.fold_left ( + ) 0;;
Printf.printf "%d\n" (sum [1;2;3;4]);;

let product = List.fold_left ( * ) 1;;
Printf.printf "%d" (product [1;2;3;4]);;
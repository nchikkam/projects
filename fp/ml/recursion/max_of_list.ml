open Printf;;

let rec max_of_list l =
	match l with 
		[] 	-> failwith "Empty List"
	| 	[x] -> x
	| 	x::xs -> max x (max_of_list xs);;

let l = [1;2;3;4;5;6;7;8;9;];;
let m = max_of_list l;;
Printf.printf "%d\n" m;;

let m = max_of_list [4];;
Printf.printf "%d" m;;

let m = max_of_list [];;
Printf.printf "%d" m;;

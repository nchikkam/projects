open List;;
open Printf;;

let l = [1;2;3;4;];;
let m = [6;7;8;9;];;

let f a b =
	Printf.printf "(%d, %d)" a b;;

List.iter2 f l m;;
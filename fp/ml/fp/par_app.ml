open List;;

(* f always has access back to its parental environment, and to n *)
let multiply n list = 
	let f x =        (* this f function here is a closure *)
		n * x in     (* n is available to f here*)
		List.map f list;;

let rec print_list = function 
	[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let () = print_list(multiply 3 [1;2;3;4;5;])
let () = print_string "\n"

(* short hand for the same above case par_app *)
let mul2ply n = List.map (( * ) n);;

let double = mul2ply 2;;
let triple = mul2ply 3;;

let () = print_list(double [1;2;3;4;5;])
let () = print_string "\n"

let () = print_list(triple [1;2;3;4;5;])
let () = print_string "\n"

(* ------------------------------------------------------------------------ *)
let plus a b =
	a + b;;

let result = plus 2 3;;
let () = print_string ( string_of_int result );;

let pluus = ( + );;
let result = pluus 2 3;;
let () = print_string "\n"

let () = print_string ( string_of_int result );;
let () = print_string "\n"

let result = List.map (pluus 2) [1;2;3;4;5];;
let () = print_list result  ;;
let () = print_string "\n"

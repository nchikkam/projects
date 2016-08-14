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
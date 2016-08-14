open List;;

let double x = x * 2 ;;

let rec print_list = function
		[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let result = List.map double [1;2;3;4;5];;

let () = print_list result;;


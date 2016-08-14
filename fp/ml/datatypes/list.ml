(* linked list *)
let rec print_list = function
		[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let l = [1;2;3;4;5]
let () = print_list l;;
let () = print_string "\n";;

let a = 1::[2;3;4;5]
let () = print_list a;;
let () = print_string "\n";;

let a = 1::[2;3;4;5]
let a = 1::2::3::4::[5;6;7;8;9]  ;; (*cons operator*)
let () = print_list a;;
let () = print_string "\n";;
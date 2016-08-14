let max a b =
	if a > b then a else b;;

let int_max 	= max 2 5;;
let float_max 	= max 2.0 5.0;;
let string_max 	= max "a" "A";;

let () = print_string (string_of_int int_max);;
let () = print_string "\n";;
let () = print_string (string_of_float float_max);;
let () = print_string "\n";;
let () = print_string (string_max);;
let () = print_string "\n";;
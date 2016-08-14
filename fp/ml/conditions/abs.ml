let abs a =
	if a >= 0 then a else -a;;

let result = abs 5;;
let () = print_string (string_of_int result);;
let () = print_string "\n"

let result = abs (-5);;
let () = print_string (string_of_int result);;
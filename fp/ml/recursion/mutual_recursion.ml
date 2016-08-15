(* 
	There are no forward declarations like in C, however
	'and' could be useful to define mutually recursive
	ones.

	The same approach like below could be useful for defining
	mutually recursive classes and modules.
*)

let rec even n =
    match n with
    | 0 -> true
    | x -> odd (x-1)
  and odd n =
    match n with
    | 0 -> false
    | x -> even (x-1);;

let () = print_string (string_of_bool (even 2));;
let () = print_string "\n";;
let () = print_string (string_of_bool (odd 2));;
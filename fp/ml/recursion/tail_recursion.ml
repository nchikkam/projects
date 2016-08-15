let rec range l h =
	if l > h then []
	else l:: range (l+1) h;;

let rec print_list = function
	[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let () = print_list (range 1 10);;
let () = print_string "\n";;


(* another style *)
let rec range1 l h =
	if l > h then []
	else 
		let result = range1 (l+1) h in 
		l:: result;;

let () = print_list (range1 1 10);;
let () = print_string "\n";;

(* tail recursion *)
let rec range2 a b accum =
    if b < a then accum
    else range2 a (b-1) (b :: accum);;

let ranget a b =
    range2 a b [];;

let () = print_list (ranget 1 10);;


(*short cuts*)
let is_even x = x mod 2 = 0;;

let is_even x =
    match x mod 2 with
    | 0 -> true
    | 1 | -1 -> false
    | _ -> assert false;;
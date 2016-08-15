let rec range ~first:a ~last:b =
	if a > b then []
	else a :: range ~first:(a+1) ~last:b;;

let rec print_list = function
	| [] -> ()
	| x::xs -> print_string ( string_of_int x); print_string " "; print_list xs;;

let () = print_list (range 1 10);;
let () = print_string "\n";;


(* we can just use ~first in which case it means ~first:first *)
let rec range2 ~first ~last =
	if first > last then []
	else first :: range (first+1) last;;

let () = print_list (range2 1 10);;

(*
	let may ~f x =
    match x with
    | None -> ()
    | Some x -> ignore(f x);;

    What is the type of the labelled f parameter? Obviously it's a function of some sort.
	What is the type of the unlabelled x parameter? The match clause gives us a clue. It's an 'a option.
	This tells us that f takes an 'a parameter, and the return value of f is ignored, so it could be anything. The type of f is therefore 'a -> 'b.
	The may function as a whole returns unit. Notice in each case of the match the result is ().
	
	its type basically is:
	may : f:('a -> 'b) -> 'a option -> unit

*)
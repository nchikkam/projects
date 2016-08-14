(* Pattern Matching *)
let f i =
	match i with
	| 1 -> "One"
	| 2 -> "Two"
	| 3 -> "Three"
	| 4 -> "Four"
	| 5 -> "Five"
	| x -> string_of_int x
let () = print_string (f 3)
let () = print_string "\n"

(* Below Code also does the same as above *)
let f = function 
	1 -> "One"
	| 2 -> "Two"
	| 3 -> "Three"
	| 4 -> "Four"
	| 5 -> "Five"
	| x -> string_of_int x

let () = print_string (f 3)


(*
	Understanding this pointless function is important. First, by using the match
	keyword, you can essentially create en extended if statement. Notice how you 
	can match specific things, like 1 and 2, and you can also match wildcards such 
	as 'x'. In the example above, if the value of i is not 1, 2, or 3, then the 
	value is bound to the variable 'x'. Then, x can be used freely.

	The arguments to function are also patterns. This is perfectly legal:
*)
let factorial 5 = 120;;

let v = (factorial 5);;
let () = print_string ( string_of_int v )


let v =  (factorial 4);;    (* This raises Exception *)
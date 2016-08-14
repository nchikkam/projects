(* an expression to human text format converter *)

type expr =
	| Plus 		of expr * expr  (* a+b *)
	| Minus 	of expr * expr 	(* a-b *)
	| Times 	of expr * expr 	(* a*b *)
	| Divide 	of expr * expr 	(* a/b *)
	| Product 	of expr list    (* means a * b * c * ... *)
	| Value 	of string		(* a, b, c etc., *)

let rec to_string e = 
	match e with
	| Plus (left, right) ->
		"(" ^ to_string left ^ " + " ^ to_string right ^ ")"
	| Minus (left, right) ->
		"(" ^ to_string left ^ " - " ^ to_string right ^ ")"
	| Times (left, right) ->
		"(" ^ to_string left ^ " * " ^ to_string right ^ ")"
	| Divide (left, right) ->
		"(" ^ to_string left ^ " / " ^ to_string right ^ ")"
	| Value v -> v;;


let print_expr e =
	print_endline (to_string e);;

print_expr (Times (Value "n", Plus(Value "x", Value "y")))


let rec multiply_out e =
    match e with
    | Times (e1, Plus (e2, e3)) ->
       Plus (Times (multiply_out e1, multiply_out e2),
             Times (multiply_out e1, multiply_out e3))
    | Times (Plus (e1, e2), e3) ->
       Plus (Times (multiply_out e1, multiply_out e3),
             Times (multiply_out e2, multiply_out e3))
    | Plus (left, right) ->
       Plus (multiply_out left, multiply_out right)
    | Minus (left, right) ->
       Minus (multiply_out left, multiply_out right)
    | Times (left, right) ->
       Times (multiply_out left, multiply_out right)
    | Divide (left, right) ->
       Divide (multiply_out left, multiply_out right)
    | Value v -> Value v;;

print_expr(multiply_out(Times (Value "n", Plus (Value "x", Value "y"))));;

let factorize e =
    match e with
    | Plus (Times (e1, e2), Times (e3, e4)) when e1 = e3 ->
       Times (e1, Plus (e2, e4))
    | Plus (Times (e1, e2), Times (e3, e4)) when e2 = e4 ->
       Times (Plus (e1, e3), e4)
    | e -> e;;

(*below does the reverse of above *)
let ex = factorize (Plus (Times (Value "n", Value "x"),
                   Times (Value "n", Value "y")));;


(*	//@ToDo:
	Exercise: Extend the pattern matching with a Product case so to_string compiles without warning.
*)
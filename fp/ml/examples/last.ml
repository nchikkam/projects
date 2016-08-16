let rec last = function
    | [] -> None
    | [x] -> Some x
    | x :: t -> last t;;

(* this method f is introduced to map None to 0, Some x to x explicitly*)
let f v =
	match v with
	| None -> 0
	| Some x -> x

let l = last [1];;
let v = f l;;

Printf.printf "%d" v;;

(*approach #2*)
let rec llast = function
	| [] -> 0
	| [x] -> x
	| x :: xs -> llast xs;;

Printf.printf "%d" (llast [1;2;3] );;
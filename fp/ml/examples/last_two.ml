let rec last_two = function
    | [] | [_] -> None
    | [x;y] -> Some (x, y)
    | x :: t -> last_two t;;

(* this method f is introduced to map None to 0, Some x to x explicitly*)
let f v =
	match v with
	| None -> (0, 0)
	| Some (x, y) -> (x, y);;

let l = last_two [1;2;3;4;5];;
let (a, b) = f l;;

Printf.printf "%d, %d" a b;;
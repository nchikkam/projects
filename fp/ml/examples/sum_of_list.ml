(*
	core std case:
	let s = List.fold_left ~f:(+) ~init:0 [1; 3; 5; 7];; 
*)

let s = List.fold_left (+) 0 [1; 3; 5; 7];;  (* using '+' operator *)
let () = print_string ( string_of_int s)


(* using function  operator *)
let add = function | []->0
                   | h::t -> List.fold_left (fun h t-> h+t) h t;;
let () = print_string ( string_of_int ( add [1;3;5;7] ) )

(* with out fold
let rec max_list smallest lst = match lst with 
    | []   -> smallest
    | h::t -> max_list (max smallest h) t;;

let () = print_string ( string_of_int ( add [1;3;5;7] ) )
*)

let rec sum (l : int list) : int =
  match l with
    [] -> 0
  | x :: xs -> x + (sum xs)

let () = print_string ( string_of_int ( sum [1;3;5;7] ) )
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


(* logic of fold *)
let rec fold_left (f: 'a -> 'b -> 'a) (acc: 'a) (l: 'b list) : 'a = 
	match l with
	| [] -> acc
	| x :: xs -> fold_left f (f acc x) xs

(* use fold left above to sum elements *)
let () = print_string ( string_of_int (fold_left (fun a s -> s + a) 0 [1;2;3;4;5] ) )


(* using fold to concatenate strings *)
let () = print_string ( fold_left (fun a s -> a ^ s) "" ["This "; "is "; "an "; "example "; "program."] )
let () = print_string ( fold_left (fun a s -> s ^ a) "" ["This "; "is "; "an "; "example "; "program."] )
let () = print_string "\n"

(* right*)
let rec fold_right (f: 'a -> 'b -> 'a) (l: 'b list) (acc: 'a): 'a =
	match l with
	| [] -> acc
	| x :: xs -> f x (fold_right f xs acc)

let () = print_string ( string_of_int (fold_right(fun a s -> s + a) [1;2;3;4;5] 0 ) )
let () = print_string ( fold_right (fun a s -> a ^ s) ["1";"2";"3";"4";"5"] "")
let () = print_string ( fold_right (fun a s -> s ^ a) ["1";"2";"3";"4";"5"] "")


(* 
	List.fold_left, List.fold_right are both curried in List module, so list argument could be ommitted 
	Both List.fold_left and List.fold_right are curried, so the list parameter can be ommitted
	---------------------------------------------------------------------------------------------------
*)
open List;;
let sum = List.fold_left (fun a x -> x + a) 0
let concat = List.fold_left (fun a x -> a ^ x) ""

let () = print_string ( string_of_int (sum [1;2;3]) );;
let () = print_string ( concat ["1";"2";"3"]) ;;

let () = print_string "\n"
(* *ml supports + and ^ operators as functions, further tuning: *)
let sum = List.fold_left (+) 0
let concat = List.fold_left (^) ""
let () = print_string ( string_of_int (sum [1;2;3]) );;
let () = print_string ( concat ["1";"2";"3"]) ;;


let length l = List.fold_left (fun a _ -> a + 1) 0 l
let rev l = List.fold_left (fun a b -> b :: a) [] l
let map f l = List.fold_right (fun x a -> (f x) :: a) l []
let app f l = List.fold_left (fun _ x -> f x) () l
let filter f l =
	List.fold_right (fun x a -> if f x then x :: a else a) l []


(* Usage: *)
let rec print_list = function 
	[] -> ()
	| e::l -> print_int e ; print_string " " ; print_list l

let () = print_string "\n"
let () = print_string ( string_of_int( length [1;2;3;4;5;6;7] ) )
let () = print_list ( rev [1;2;3;4;5;6;7] )
let () = print_string "\n"
let () = print_list ( map (fun a -> a + 10) [1;2;3;4;5;6;7] )
let () = print_string "\n"
let () = print_list ( filter (fun a -> true) [1;2;3;4;5;6;7] )
let () = print_string "\n"
let () = print_list ( filter (fun a -> false) [1;2;3;4;5;6;7] )
let () = print_string "\n"
let () = print_list ( filter (fun a -> (a mod 2)=0 ) [1;2;3;4;5;6;7] )
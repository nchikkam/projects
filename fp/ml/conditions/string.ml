open Printf;;

(* splits the string to char list*) 
let explode s =
  let rec exp i l =
    if i < 0 then l else exp (i - 1) (s.[i] :: l) in
  exp (String.length s - 1) [];;

(* joins the char list to string *) 
let implode l =
  let res = String.create (List.length l) in
  let rec imp i = function
  | [] -> res
  | c :: l -> res.[i] <- c; imp (i + 1) l in
  imp 0 l;;

let rec print_list = function
	[] -> ()
	| x::xs -> print_string x; print_string "\n"; print_list xs;;

let r = explode "abcdefgh";;
(* let () = print_list (implode r);; *)
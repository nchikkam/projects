let rev list =
    let rec aux acc = function
      | [] -> acc
      | h::t -> aux (h::acc) t in
    aux [] list;;

let rec print_list = function
  | [] -> 0
  | x :: xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let l = [1;2;3;4;5;4;3;2;1] ;;
let r = rev l;;


(* auxiliaries to find comparison *)
let rec compareVs v1 v2 = match v1, v2 with
  | [], []       -> true
  | [], _
  | _, []        -> false
  | x::xs, y::ys -> x = y && compareVs xs ys;;


print_list l;;
print_string "\n";;
print_list r;;

Printf.printf "\n%s" (string_of_bool (compareVs l r) );;

(* short cut*)
let is_palindrome list =
    list = List.rev list;;

Printf.printf "\n%s" (string_of_bool (is_palindrome l) );;
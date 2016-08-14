
let give_me_a_five _ = 3;;

(* below works fine *)
let () = print_string ( string_of_int (give_me_a_five 1000) );;

(* below causes Exception: Division_by_zero. *)
let () = print_string ( string_of_int (give_me_a_five 1/0) );;


(* using lazy to enable lazy evaluation*)
open Lazy;;

let lazy_expr = lazy (1/0);;
Lazy.force lazy_expr ;;
(* below just passes *)
let () = print_string ( string_of_int (lazy_expr 1/0) );;
(* force to strict enable lazy *)

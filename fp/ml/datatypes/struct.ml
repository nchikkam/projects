(* struct *)
type pair = {a: int; b: int};;

{a=10; b=15;};;  (* OK*)

{a=12};;         (* NOT OK, all fields must be initialized in this scenario*)
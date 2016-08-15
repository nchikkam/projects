type lock = Open | Close
type door = Open | Close;;

(* 
	Open 's type becomes door due to latest definition by type inference:
	To have all the definitions, there is a special syntax:
*)

type lock = [ `Open | `Close ];;
type door = [ `Open | `Close ];;

let print_lock st =				(* to findout the type of enum at runtime *)
    match st with
    | `Open -> print_endline "The lock is open"
    | `Close -> print_endline "The lock is closed";;

print_lock `Open;;
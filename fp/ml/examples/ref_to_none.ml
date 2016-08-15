
(*
	raises:
	The type of this expression... contains type variables that cannot be generalized


*)
let x = ref None;;

(*solution: *)
let x : string option ref = ref None;;

(*or*)
let x = ref (None : string option);;

x := Some 0;;  (*note: assigninng to a ref needs ':='' operator *)
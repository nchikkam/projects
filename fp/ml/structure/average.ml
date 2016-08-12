(* 	Local "variables" (really local expressions)

	let ... in 
*)
let average a b = 
	let sum = a +. b in sum /. 2.0;;             (* ;; ends the sum definition block*)

let () = print_string (string_of_float (average 2.0 4.0))

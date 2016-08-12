(* 	Local "variables" (really local expressions)
	let ... in 

	let f a b =
	(a +. b) +. (a +. b) ** 2.;;
*)

let f a b =
	let x = (a +. b) in 
	x +. x ** 2. ;;


let () = print_string (string_of_float (f 2.0 4.0))
(*
	The example shown runs faster than the (a+b) + (a+b)**2 as most compilers
	do this optimization at the compilation level - its called constant folding.
*)
let average a b = 
	(a +. b) /. 2.0
	;;

let () = print_string (string_of_float (average 2.0 4.0) )
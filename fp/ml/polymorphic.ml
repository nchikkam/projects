(* 	polymorphic function example: a function that takes
  	any type as parameter, but returns a specifigc type
	the type of the below function is 

	give_me_a_three_style2 : 'a -> int 

	Note the the single quote before a denotes that the 
	function can accept any type variable as argument.

*)
let give_me_a_three x = 3

let () = print_string (string_of_int(give_me_a_three "foo"))
let () = print_string (string_of_int(give_me_a_three 2.0))
let () = print_string (string_of_int(give_me_a_three [1, 2, 3]))

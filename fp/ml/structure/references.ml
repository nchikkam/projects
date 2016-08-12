(* 	
	The := operator is used to assign to references, and the 
	! operator dereferences to get out the contents. 
*)

let my_ref = ref 0;;   (* int a = 0, *my_ref = &a;	*)
my_ref := 100;;        (* *my_ptr = 100; 			*)

let () = print_string (string_of_int(!my_ref+100))  (* !derefences *)
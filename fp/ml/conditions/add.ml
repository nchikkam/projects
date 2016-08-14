let add a b =
	a + if b> 0 then b else 0;;

let r =  add 2 3;;
let () = print_string (string_of_int r);
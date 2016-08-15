let rec range ?(step=1) a b =
	if a > b then []
	else a:: range ~step (a+step) b;;

let rec print_list = function
	[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let () = print_list (range 1 10);;
let () = print_string "\n";;
let () = print_list (range 1 10 ~step:2);;

(*
		When an optional parameter doesn't have a default, then it has type 'a option. 
		The 'a would normally be inferred by type inference

		eg:
		let open_window ?title ?width ?height () =
	    let window = create_window () in
	    may ~f:(set_title window) title;
	    may ~f:(set_width window) width;
	    may ~f:(set_height window) height;
	    window;;

		val open_window :
		?title:string -> ?width:int -> ?height:int -> unit -> window = <fun>

		in case of optional arguments and partial functions, compiler doesn't
		know if it was a function call or in the mid of currying.

		so this is partial app:
		# open_window;;

		and this is invocation:
		open_window ();;
*)
module Hello: sig
	val hello : unit -> unit
end = 
struct 
	let message = "Hello"
	let hello () = print_endline message
end

(* At this point, Hello.message is not accessible anymore. *)
let goodbye () = print_endline "Goodbye"
let hello_goodbye () = 
	Hello.hello ();
	goodbye ()

(*
	In general module signatues are defined seperately in a .mli file like below:
	module type Hello_type = sig
		val hello : unit -> unit
	end

	module Hello: Hello_type = struct 
	...
	end
*)
(*
	Nested functions: 
	The form for nested functions is the same as for local named expressions: 

	let <name> <arguments> = <function-definition>
	in
	<code>
*)
let f a b =
	let exponent x y = 
		x ** y
	in
	let x = (a +. b) in 
	x +. exponent x 2.0 ;;

(*

let read_whole_channel chan =
    let buf = Buffer.create 4096 in
    let rec loop () =
      let newline = input_line chan in
      Buffer.add_string buf newline;
      Buffer.add_char buf '\n';
      loop ()
    in
    try
      loop ()
    with
      End_of_file -> Buffer.contents buf;;
*)

let () = print_string (string_of_float(f 2.0 4.0))
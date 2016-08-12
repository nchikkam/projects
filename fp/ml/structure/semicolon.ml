(* 	
	Ocaml is smart enough to identify the a statment ended at a toplevel
	when it sees a missing ';;'. 

	There specific rules where to use elide ';;' and where to elide ';;':
	Rule #1 is that you should use ;; to separate statements at the top-level of your code, and never within function definitions or any other kind of statement.
    ----------------
	Have a look at a section from the second graphics example above:

	Random.self_init ();;
	Graphics.open_graph " 640x480";;

	let rec iterate r x_init i =
	  if i = 1 then x_init
	  else
	    let x = iterate r x_init (i-1) in
	    r *. x *. (1.0 -. x);;
	We have two top-level statements and a function definition (of a function called iterate). Each one is followed by ;;.

	Rule #2 is that sometimes you can elide the ;;. As a beginner you shouldn't worry about this — you should always put in the ;; as directed by Rule #1. But since you'll also be reading a lot of other peoples' code you'll need to know that sometimes we can elide ;;. The particular places where this is allowed are:
	-------------------
	Before the keyword let.
	Before the keyword open.
	Before the keyword type.
	At the very end of the file.
	A few other (very rare) places where OCaml can "guess" that the next thing is the start of a new statement and not the continuation of the current statement.
	Here is some working code with ;; elided wherever possible:

	refer to the graphics_omit*.ml program for more details. Its self explanatory.

	Rules #3 and #4 refer to the single ;. This is completely different from ;;. The single semicolon ; is what is known as a sequence point, which is to say it has exactly the same purpose as the single semicolon in C, C++, Java and Perl. It means "do the stuff before this point first, then do the stuff after this point when the first stuff has completed". Bet you didn't know that.
	Rule #3 is: Consider let ... in as a statement, and never put a single ; after it.
	Rule #4 is: For all other statements within a block of code, follow them with a single ;, except for the very last one.


*)

(* 
	';' is an operator, all the below statements mean the same thing. 
	All the below statements mean the same thing:

*)

let f x b y = if b then x+y else x+0
let () = print_string (string_of_int(f 2 false 3) )
let () = print_string (string_of_int(f 2 true 3) )

let f1 x b y = x + (if b then y else 0)
let () = print_string (string_of_int(f1 2 false 3) )
let () = print_string (string_of_int(f1 2 true 3) )

let f x b y = x + (match b with true -> y | false -> 0)
let () = print_string (string_of_int(f 2 false 3) )
let () = print_string (string_of_int(f 2 true 3) )

let f x b y = x + (let g z = function true -> z | false -> 0 in g y b)
let () = print_string (string_of_int(f 2 false 3) )
let () = print_string (string_of_int(f 2 true 3) )

let f x b y = x + (let _ = y + 3 in (); if b then y else 0);;     (* this highlights how ';'' could be used for joining 2 statments. like ',' in 'C' *)
let () = print_string (string_of_int(f 2 false 3) )
let () = print_string (string_of_int(f 2 true 3) )


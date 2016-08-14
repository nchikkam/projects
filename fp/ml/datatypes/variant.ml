(* variant - unions in 'C' 
   in 'C':
   1:
	
	struct bit_fields {
		  int type;
		  union {
		    int i;
		    int pair[2];
		    char *str;
		  } u;
		};

	First part of each | separated part is called the constructor. It can be called
	anything, as long as it starts with a capital letter.
*)

type bit_fields =
    | Nothing
    | Int of int
    | Pair of int * int
    | String of string;;

(*
	2: enums 
	in 'C':
	enum sign { positive, zero, negative };
*)

type sign = Positive | Zero | Negative;;


(* 
	3: 
	recursive variants
*)
type binary_tree = 
	| Leaf of int
	| Tree of binary_tree * binary_tree;;


(*
	4: 
	Parameterized variants (same as recursive but with polymorphic type)
*)
type 'a binary_tree = 
	| Leaf of 'a
	| Tree of 'a binary_tree * 'a binary_tree;;

(*
	using the inference system to identify the type of Node in the Tree:

	# type 'a bt =
        | Leaf of 'a
        | Tree of 'a bt * 'a bt;;
	type 'a bt = Leaf of 'a | Tree of 'a bt * 'a bt

	# Leaf "hello";;
	- : string bt = Leaf "hello"

	# Leaf 3.0;;
	- : float bt = Leaf 3.
	
	type 'a list = [] | :: of 'a * 'a list   (* not real OCaml code *)


*)

type 'a equiv_list = 
	| Nil
	| Cons of 'a * 'a equiv_list;;

(*
	# Cons(1, Nil);;
	- : int el = Cons (1, Nil)
	# Cons(1, Cons(2, Cons(3, Nil)));;
	- : int el = Cons (1, Cons (2, Cons (3, Nil)))
	#
*)

(*
	Summary: 
	list           int list                       [1; 2; 3]
	tuple          int * string                   (3, "hello")
	record         type pair =                    { a = 3; b = "hello" }
	                 { a: int; b: string }
	variant        type foo =
	                 | Int of int                 Int 3
	                 | Pair of int * string
	variant        type sign =
	                 | Positive                   Positive
	                 | Zero                       Zero
	                 | Negative
	parameterized  type 'a my_list =
	variant          | Empty                      Cons (1, Cons (2, Empty))
	                 | Cons of 'a * 'a my_list
*)
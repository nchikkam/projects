(* 
	There is no nested list type in OCaml, so we need to define one
	first. A node of a nested list is either an element, or a list of
	nodes
*)
type 'a node =
  | One of 'a 
  | Many of 'a node list;;

let flatten list =
    let rec aux acc = function
      | [] -> acc
      | One x :: t -> aux (x :: acc) t
      | Many l :: t -> aux (aux acc l) t in
    List.rev (aux [] list);;

let result = flatten [ 	One "a" ; 
			Many [	One "b" ; 
					Many [	One "c" ;
							One "d" 
					] ; 
					One "e" 
				]
		];;

let rec print_list = function
  | [] -> ()
  | x :: xs -> Printf.printf "%s" x; print_list xs;;

let () = print_list result;;
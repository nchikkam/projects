(*
	let buckets = Hashtbl.create <capacity>;;
*)

let buckets = Hashtbl.create 100;;

Hashtbl.add buckets "h" "hello";;
Hashtbl.add buckets "h" "hi";;
Hashtbl.add buckets "h" "hug";;
Hashtbl.add buckets "h" "hard";;
Hashtbl.add buckets "w" "wimp";;
Hashtbl.add buckets "w" "world";;
Hashtbl.add buckets "w" "wine";;

let result = Hashtbl.find buckets "h";;
let () = print_string result;;
let () = print_string "\n";;


let result = Hashtbl.find_all buckets "h";;     (* interesting, keeps all populations*)

let rec print_list = function 
	[] -> ()
	| x::xs -> print_string x; print_string " "; print_list xs;;

let () = print_list result
let () = print_string "\n";;

(* If you remove a key, its previous value becomes again the default one associated to the key.*)
Hashtbl.remove buckets "h";;   
let () = print_list result
let () = print_string "\n";;

let result = Hashtbl.find buckets "h";;
let () = print_string result;;
let () = print_string "\n";;


Hashtbl.replace buckets "t" "tree";;
Hashtbl.replace buckets "t" "test";;
let result = Hashtbl.find_all buckets "t";;
let () = print_list result;;
let () = print_string "\n";;


Hashtbl.remove buckets "t";
Hashtbl.find buckets "t";;    (* Exceptoin Not_Found *)

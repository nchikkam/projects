module SS = Set.Make(String);;

let s = SS.empty;;

let s = SS.singleton "Test Sample";;

let s = 
	List.fold_right SS.add ["one";"two";"three";"four";"five";"six";"seven";"eight";"nine";"ten"] s;;

let print_set s = 
     SS.iter print_endline s;;

let () = print_set s;;

let my_filter str = 
	String.length str <= 5;;

let s2 = SS.filter my_filter s;;

let s2 = SS.filter (fun str -> String.length str <= 5) s;;
(* check membership *)

SS.mem "hello" s;; 

print_set (SS.diff s s2);;
(* create a map <String, String> *)
module NumbersMap = Map.Make(String);;

(* creates empty map*)
let m = NumbersMap.empty;;  

(* add elements *)
let m = NumbersMap.add "One"  1 m;;
let m = NumbersMap.add "Two"  2 m;;

(* function to humanize the output when passed to iter*)
let print_users key value =
    print_string(key ^ " " ^ ( string_of_int value ) ^ "\n");;

NumbersMap.iter print_users m;;


let result = NumbersMap.find "One" m;;
let () = print_string ( string_of_int result )


(* generates exception 'Exception: Not_found.'*)
let result = NumbersMap.find "Two" m;;
let () = print_string ( string_of_int result )


let () = print_string ( string_of_int (NumbersMap.cardinal m))


let rm = NumbersMap.remove "Two" m;;

let () = print_string ( string_of_int (NumbersMap.cardinal rm))

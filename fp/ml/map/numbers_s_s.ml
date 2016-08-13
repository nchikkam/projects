(* create a map <String, String> *)
module NumbersMap = Map.Make(String);;

(* creates empty map*)
let m = NumbersMap.empty;;  

(* add elements *)
let m = NumbersMap.add "1"  "One" m;;
let m = NumbersMap.add "2"  "Two" m;;
let m = NumbersMap.add "3"  "Three" m;;
let m = NumbersMap.add "4"  "Four" m;;
let m = NumbersMap.add "5"  "Five" m;;
let m = NumbersMap.add "6"  "Six" m;;
let m = NumbersMap.add "7"  "Seven" m;;
let m = NumbersMap.add "8"  "Eight" m;;
let m = NumbersMap.add "9"  "Nine" m;;
let m = NumbersMap.add "10" "Ten" m;;

(* function to humanize the output when passed to iter*)
let print_users key value =
    print_string(key ^ " " ^ value ^ "\n");;

NumbersMap.iter print_users m;;


let result = NumbersMap.find "10" m;;
let () = print_string result


(* generates exception 'Exception: Not_found.'*)
let result = NumbersMap.find "12" m;;
let () = print_string result
let rev list =
    let rec aux acc = function
      | [] -> acc
      | h::t -> aux (h::acc) t in
    aux [] list;;

let rec print_list = function
  | [] -> 0
  | x :: xs -> print_string (string_of_int x); print_string " "; print_list xs;;

let r = rev [1;2;3;4;5;6;7;8;9;] ;;

print_list r;;
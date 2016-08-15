let rec last = function
    | [] -> None
    | [x] -> x
    | x :: t -> last t;;

let l = last [1];;

let () = print_string (string_of_int l);;
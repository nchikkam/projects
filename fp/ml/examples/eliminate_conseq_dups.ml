(*eliminate consequitive duplicates*)
let rec compress = function
  | a :: (x :: _ as t) -> if a = x then compress t else a :: compress t
  | smaller -> smaller;;

let rec print_list = function
  | [] -> ()
  | x :: xs -> print_string x; print_string " "; print_list xs;;

let result = compress ["a";"a";"a";"a";"b";"c";"c";"a";"a";"d";"e";"e";"e";"e"];;

print_list result;;
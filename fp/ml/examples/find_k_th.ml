let rec find_kth k = function
  | [] -> None
  | x :: xs -> if k = 1 then Some x else find_kth (k-1) xs;;

let find = function
  | None -> 0
  | Some x -> x;;

let k = find_kth 3 [1;2;58;4;5;6;7;8;9;];;
let v = find k;;


Printf.printf "%d" v;;
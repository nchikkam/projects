let rec len = function
  | [] -> 0
  | [x] -> 1 
  | x :: xs -> 1 + len xs;;

Printf.printf "%d\n" (len [1;2;3;4;5]);;

(* This function is tail-recursive: it uses a constant amount of
     stack memory regardless of list size. *)
  let length list =
    let rec aux n = function
      | [] -> n
      | _::t -> aux (n+1) t
    in aux 0 list;;

Printf.printf "%d" (length [1;2;3;4;5]);;
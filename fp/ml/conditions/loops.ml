
for i = 1 to 10 do
	(* let () = print_string (string_of_int i) *)
	i
done;;

(* -------------------------------------------------------  *)
let quit_loop = ref false in
while not !quit_loop do
  print_string "Have you had enough yet? (y/n) ";
  let str = read_line () in
  if str.[0] = 'y' then
    quit_loop := true
done;;

(* -------------------------------------------------------  *)
open Printf;;

let l = [1;2;3;4;5;6;7;8;9;10];;

let f elem = 
	Printf.printf "%d\n" elem in 
	List.iter f l;;
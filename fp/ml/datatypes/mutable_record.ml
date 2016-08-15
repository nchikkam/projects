type pair = {x: int; y: int};;

let print_pair pair =
	print_endline ("x = " ^ string_of_int pair.x ^ ", y = " ^ string_of_int pair.y);;

let () = print_pair {x=20; y=15;};;

let point = {x=2; y=3;};;

let () = print_endline( string_of_int point.x ^ string_of_int point.y);;

(*
point.x <- point.x + 1;;  (* will report: Error: The record field x is not mutable *)
*)


(* with mutable speciifier a field of a record could be modifiable *)
type employee = {name: string; mutable age: int};;
let print_employee employee =
	print_endline ("name = " ^ employee.name ^ ", age = " ^ string_of_int employee.age);;


let member = {name="scott"; age=27;};;
let () = print_employee member;;

member.age <- member.age + 1;;
let () = print_employee member;;
open Array;;

let a = Array.create 10 0;;

for i = 0 to Array.length a - 1 do
	a.(i) <- i
done;;

for i = 0 to Array.length a - 1 do
	print_string ( string_of_int a.(i) )
done;;

(* 
	Arrays are denoted in the below style: note the '|'s.	
	[|0; 1; 2; 3; 4; 5; 6; 7; 8; 9|] 
*)
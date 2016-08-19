let rec ncr n k = 
	if n = k then 1
	else if n = 0 then 1
	else if k = 0 then 1
	else ( ncr (n-1) (k-1) ) + ( ncr (n-1) (k) )

let () = print_string ( string_of_int (ncr 52 5) );;
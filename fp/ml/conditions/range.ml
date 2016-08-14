let rec range l h = 
	if l > h then []
	else l:: range (l+1) h;;

let r = range 1 10;;

let rec print_list = function
		[] -> ()
	| x::xs -> print_string (string_of_int x); print_string " "; print_list xs;;

print_list r;;
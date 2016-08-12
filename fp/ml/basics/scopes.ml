let positive_sum a b = 
    let a = max a 0			(* a b become old bindins for new a*)
    and b = max b 0 in
    a + b;;					

let () = print_string (string_of_int(positive_sum 3 5))
let rec range a b =
      if a > b then []
      else a :: range (a+1) b;;
let () = print_string (String.concat " " (List.map string_of_int (range 1 10)))


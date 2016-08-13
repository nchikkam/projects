open Printf
let my_data = ["an"; "example"; "snippet"; "code"]
let () = List.iter (fun s -> printf "%s\n" s) my_data;;
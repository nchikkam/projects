(*
let rec read_directory path =
    let dirh = opendir path in
    let rec loop () =
      let filename = readdir_no_ex dirh in
      match filename with
      | None -> []
      | Some "." -> loop ()
      | Some ".." -> loop ()
      | Some filename ->
          let pathname = path ^ "/" ^ filename in
          let stat = lstat pathname in
          let this = if stat.st_kind = S_DIR then
                       read_directory pathname
                     else
                       File pathname in
          this :: loop () in
    Directory (loop ());;
*)

(* or 
let rec read_filesystem path =
    if (lstat path).st_kind = S_DIR then
      Directory (read_directory path)
    else
      File path
    
  and read_directory path =
    let dirh = opendir path in
    let rec loop entries =
      try
        match readdir dirh with
        | "." | ".." -> loop entries
        | filename ->
           loop (read_filesystem (path ^ "/" ^ filename) :: entries)
      with End_of_file -> entries in
    let list = loop [] in
    closedir dirh;
    list;;
*)

let list = ref [] in
let dir = opendir "......." in
try
  while true do
    match readdir dir with
    | "." | ".." -> ()
    | filename -> list := filename :: !list
  done;
  assert false
with End_of_file -> !list


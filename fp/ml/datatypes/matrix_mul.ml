let size = 30
  
  let mkmatrix rows cols =
    let count = ref 1
    and last_col = cols - 1
    and m = Array.make_matrix rows cols 0 in
    for i = 0 to rows - 1 do
      let mi = m.(i) in
      for j = 0 to last_col do
        mi.(j) <- !count;
        incr count
      done;
    done;
    m
  
  let rec inner_loop k v m1i m2 j =
    if k < 0 then v
    else inner_loop (k - 1) (v + m1i.(k) * m2.(k).(j)) m1i m2 j
  
  let mmult rows cols m1 m2 m3 =
    let last_col = cols - 1
    and last_row = rows - 1 in
    for i = 0 to last_row do
      let m1i = m1.(i) and m3i = m3.(i) in
      for j = 0 to last_col do
        m3i.(j) <- inner_loop last_row 0 m1i m2 j
      done;
    done
  
  let () =
    let n =
      try int_of_string Sys.argv.(1)
      with Invalid_argument _ -> 1
    and m1 = mkmatrix size size
    and m2 = mkmatrix size size
    and m3 = Array.make_matrix size size 0 in
    for i = 1 to n - 1 do
      mmult size size m1 m2 m3
    done;
    mmult size size m1 m2 m3;
    Printf.printf "%d %d %d %d\n" m3.(0).(0) m3.(2).(3) m3.(3).(2) m3.(4).(4);;
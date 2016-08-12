(* 
	Run the below command line before running this program:
	ocamlmktop -o ocaml-graphics graphics.cma

	This basically bring that module to the current directory
	for windows users.

*)

(* To compile this example: ocamlc graphics.cma graphics_example.ml -o graphics_example *)
open Graphics;;

open_graph " 640x480";;
for i = 12 downto 1 do
  let radius = i * 20 in
  set_color (if i mod 2 = 0 then red else yellow);
  fill_circle 320 240 radius
done;;
read_line ();;


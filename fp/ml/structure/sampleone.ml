(* 
	First snippet 
	The programmer opens a couple of standard libraries (eliding the ;; because the 
	next keyword is open and let respectively). He then creates a function called 
	file_dialog. Inside this function he defines a named expression called sel using 
	a two-line let sel = ... in statement. Then he calls several methods on sel.
*)
open StdLabels
open GMain

let file_dialog ~title ~callback ?filename () =
  let sel =
    GWindow.file_selection ~title ~modal:true ?filename () in
  sel#cancel_button#connect#clicked ~callback:sel#destroy;
  sel#ok_button#connect#clicked ~callback:do_ok;
  sel#show ()

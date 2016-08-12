(* 
	Second snippet 
	Just a long list of global names at the top level. Notice that the author 
	elided every single one of the ;; because of Rule #2
*)
let window = GWindow.window ~width:500 ~height:300 ~title:"editor" ()
let vbox = GPack.vbox ~packing:window#add ()

let menubar = GMenu.menu_bar ~packing:vbox#pack ()
let factory = new GMenu.factory menubar
let accel_group = factory#accel_group
let file_menu = factory#add_submenu "File"
let edit_menu = factory#add_submenu "Edit"

let hbox = GPack.hbox ~packing:vbox#add ()
let editor = new editor ~packing:hbox#add ()
let scrollbar = GRange.scrollbar `VERTICAL ~packing:hbox#pack ()(* Second snippet *)
let window = GWindow.window ~width:500 ~height:300 ~title:"editor" ()
let vbox = GPack.vbox ~packing:window#add ()

let menubar = GMenu.menu_bar ~packing:vbox#pack ()
let factory = new GMenu.factory menubar
let accel_group = factory#accel_group
let file_menu = factory#add_submenu "File"
let edit_menu = factory#add_submenu "Edit"

let hbox = GPack.hbox ~packing:vbox#add ()
let editor = new editor ~packing:hbox#add ()
let scrollbar = GRange.scrollbar `VERTICAL ~packing:hbox#pack ()

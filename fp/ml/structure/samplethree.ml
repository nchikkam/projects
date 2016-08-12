(* 
  Third snippet 
  The author imports all the symbols from the GdkKeysyms module. Now we have
  an unusual let-binding. let _ = expression means "calculate the value of the 
  expression (with all the side-effects that may entail), but throw away the 
  result". In this case, "calculate the value of the expression" means to run 
  Main.main () which is Gtk's main loop, which has the side-effect of popping 
  the window onto the screen and running the whole application. The "result" of
  Main.main () is insignificant - probably a unit return value, but I haven't 
  checked - and it doesn't get returned until the application finally exits.

  Notice in this snippet how we have a long series of essentially procedural 
  commands. This is really a classic imperative program.
*)
open GdkKeysyms

let () =
  window#connect#destroy ~callback:Main.quit;
  let factory = new GMenu.factory file_menu ~accel_group in
  factory#add_item "Open..." ~key:_O ~callback:editor#open_file;
  factory#add_item "Save" ~key:_S ~callback:editor#save_file;
  factory#add_item "Save as..." ~callback:editor#save_dialog;
  factory#add_separator ();
  factory#add_item "Quit" ~key:_Q ~callback:window#destroy;
  let factory = new GMenu.factory edit_menu ~accel_group in
  factory#add_item "Copy" ~key:_C ~callback:editor#text#copy_clipboard;
  factory#add_item "Cut" ~key:_X ~callback:editor#text#cut_clipboard;
  factory#add_item "Paste" ~key:_V ~callback:editor#text#paste_clipboard;
  factory#add_separator ();
  factory#add_check_item "Word wrap" ~active:false
    ~callback:editor#text#set_word_wrap;
  factory#add_check_item "Read only" ~active:false
    ~callback:(fun b -> editor#text#set_editable (not b));
  window#add_accel_group accel_group;
  editor#text#event#connect#button_press
    ~callback:(fun ev ->
      let button = GdkEvent.Button.button ev in
      if button = 3 then begin
        file_menu#popup ~button ~time:(GdkEvent.Button.time ev); true
      end else false);
  editor#text#set_vadjustment scrollbar#adjustment;
  window#show ();
  Main.main ()

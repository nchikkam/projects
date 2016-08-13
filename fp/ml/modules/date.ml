type date = { day : int;  month : int;  year : int }

(*
 four options when it comes to writing the .mli file:

	The type is completely omitted from the signature.
	The type definition is copy-pasted into the signature.
	The type is made abstract: only its name is given.
	The record fields are made read-only: type date = private { ... }

	In case 3, it would be the following code:

	type date

	Now, users of the module can manipulate objects of type date, but they can't access 
	the record fields directly. They must use the functions that the module provides. 
	Let's assume the module provides three functions, one for creating a date, one for 
	computing the difference between two dates, and one that returns the date in years:

	refer to date.mli file for more details.

*)
(* adding only few methods to manipulate the date, users can create, sub or years and nothing else.*)
type date 
val create : ?days:int -> ?months:int -> ?years:int -> unit -> date
val sub : date -> date -> date
val years : date -> float

(*
	The point is that only create and sub can be used to create date records.
	Therefore, it is not possible for the user of the module to create ill-formed records. 
	Actually, our implementation uses a record, but we could change it and be sure that 
	it will not break any code that relies on this module! This makes a lot of sense 
	in a library since subsequent versions of the same library can continue to expose the 
	same interface, while internally changing the implementation, including data structures.
*)
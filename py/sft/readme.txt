readme.txt
-------------------------------------------------------------------------------
This project is a simple variation of fizzbuzz program. It has been organized 
to have the subcomponents in their respective library packages so as to manage
the project in an easy way keeping the changes to one module and testing it 
individualy for individual changes and integration testing it once the sub-
component has been tested properly.

The project has the below directory structure:

		|
		+----- lib
		|		|
		|		+----- __init__.py 		(standard python module file)
		|		|
		|		|
		|		+----- fib.py          	(This module holds the logic for fibonacci
		|		|														 method)
		|		|
		|		|
		|		+----- prime.py         (This module holds the logic for checking 
		|		|												prime validity)
		|		|
		|		|
		|		+----- fizzbuzz.py 		(This module holds the logic of fizzbuzz 
		|		|													prime logic)
		|		|
		|		+----- util.py 			(A third party kind of module to keep 
		|															helpers)
		|
		|
		|
		+----- fibtests.py 				(tests for the fib.py methods and related 
		|																things)
		|
		+----- primetests.py 			(tests for prime or not validity)
		|
		+----- fizzbuzztests.py         (tests for fizzbuzz logic verification)
		|
		+----- fib_fizzbuzz.py          (Main driver application)

Below are the command line examples to run this application:
Run#1:
-------------------------------------------------------------------------------
C:\Python27\python.exe fib_fizzbuz.py --number 9
FizzBuzz
1
1
BuzzFizz
Buzz
Fizz
8
BuzzFizz
Buzz
34

Run#2:
-------------------------------------------------------------------------------
C:\Python27\python.exe fib_fizzbuz.py --number 20
FizzBuzz
1
1
BuzzFizz
Buzz
Fizz
8
BuzzFizz
Buzz
34
Fizz
BuzzFizz
Buzz
BuzzFizz
377
Fizz
Buzz
BuzzFizz
2584
4181

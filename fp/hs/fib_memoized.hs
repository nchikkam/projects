fib j   = fiblist !! j
fiblist = map f [ 0 .. ]
          where f 0 = 0
                f 1 = 1
                f i = fiblist !! (i - 1) + fiblist !! (i - 2)
main = print (fib 20)
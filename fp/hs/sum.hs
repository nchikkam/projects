sum1 [] = 0
sum1 (x:xs) = x + sum1 xs

--sum2 = foldr (+) 0 -- short cut

main = print ( sum1 [1, 2, 3, 4, 5] )
divisors :: Integer -> [Integer]

divisors 1 = [1]

divisors x = 1:[ y | y <- [2..(x `div` 2)], x `mod` y == 0] ++ [x]

main = print (divisors 30)
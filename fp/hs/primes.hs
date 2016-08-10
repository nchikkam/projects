-- divisors logic
divisors :: Integer -> [Integer]
divisors 1 = [1]
divisors x = 1:[ y | y <- [2..(x `div` 2)], x `mod` y == 0] ++ [x]

-- is prime logic, doesn't use sqrt
isPrime :: Integer -> Bool
isPrime x = divisors x == [1,x]

-- primes
primes :: [Integer]
primes = [ x | x <- [2..], isPrime x]

main = print ( primes )
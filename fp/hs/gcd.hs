gcd1 a 0 = a
gcd1 a b = b `seq` gcd1 b (a `mod` b) where

main = print ( gcd1 70 28 )
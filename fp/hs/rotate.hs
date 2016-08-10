rotate :: [a] -> Int -> [a]
rotate [] _ = []
rotate xs 0 = xs
rotate (x:xs) n 
 | n > 0 = rotate (xs++[x]) (n-1)
 | otherwise = rotate (x:xs) (length (x:xs) + n)

 main = print ( rotate ['a','b','c','d','e','f','g','h'] (-2) )
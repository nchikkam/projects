multiply [] = 1
multiply (x:xs) = x * multiply xs


-- mul = foldr (*) 1 --short cut
main = print ( multiply [1, 2, 3, 4, 5] )